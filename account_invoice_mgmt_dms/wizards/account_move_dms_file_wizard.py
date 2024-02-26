# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, _
import base64
import pytesseract
from pdf2image import convert_from_path
import tempfile


class AccountMoveDmsFileWizard(models.TransientModel):
    _name = 'account.move.dms.file.wizard'
    _description = 'account.move.dms.file.wizard'

    account_move_id = fields.Many2one('account.move')
    dms_file = fields.Binary("Attachment")
    dms_file_name = fields.Char()

    def save_account_move_dms(self):
        directory_id = self.env.ref('account_invoice_mgmt_dms.dms_directory_puchase_invoice')
        extension_name = self.dms_file_name.split(".")[-1]
        extension_size = -(len(extension_name)) - 1
        name = self.dms_file_name[:extension_size]

        self.account_move_id.dms_file_ids.unlink()

        proceeding = ''
        for purchase_order_id in self.account_move_id.invoice_line_ids.purchase_line_id.order_id:
            ticket_id = self.env["stock.picking.classification"].sudo().search([("picking_id.classification_purchase_order_id", "=", purchase_order_id.id)]).picking_id.move_ids_without_package
            if ticket_id:
                if not proceeding == '':
                    proceeding = '%s, %s' % (proceeding, ticket_id.picking_id.name)
                else:
                    proceeding = ticket_id.picking_id.name

        if not proceeding:
            proceeding = self.account_move_id.name

        dms_file_name = '%s_%s_%s.%s' % (name, (self.account_move_id.ref).replace("/", ""), (self.account_move_id.name).replace("/", ""), extension_name)

        dms_file_id = self.env['dms.file'].sudo().create({
            'name': dms_file_name,
            'content': self.dms_file,
            'directory_id': directory_id.id,
            'proceeding': proceeding,
            'account_move_id': self.account_move_id.id
        })

        pdf_data = base64.b64decode(self.dms_file)

        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=True) as temp_pdf:
            temp_pdf.write(pdf_data)
            temp_pdf.flush()
            images = convert_from_path(temp_pdf.name)

            dms_file_id.ocr_doc = ''
            for i, image in enumerate(images):
                text = pytesseract.image_to_string(image, lang='spa', config='--psm 6')
                dms_file_id.ocr_doc += _('Page %s: %s <br/><br/>') % (i+1, text)
