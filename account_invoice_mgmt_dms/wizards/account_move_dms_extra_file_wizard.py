# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, _


class AccountMoveDmsExtraFileWizard(models.TransientModel):
    _name = 'account.move.dms.extra.file.wizard'
    _description = 'account.move.dms.extra.file.wizard'

    account_move_id = fields.Many2one('account.move')
    dms_file = fields.Binary("Attachment")
    dms_file_name = fields.Char()

    def save_account_move_dms_extra(self):
        directory_id = self.env.ref('account_invoice_mgmt_dms.dms_directory_extra_doc')
        extension_name = self.dms_file_name.split(".")[-1]
        extension_size = -(len(extension_name)) - 1
        name = self.dms_file_name[:extension_size]

        self.account_move_id.complete_proceesing_id.unlink()

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

        self.env['dms.file'].sudo().create({
            'name': dms_file_name,
            'content': self.dms_file,
            'directory_id': directory_id.id,
            'proceeding': proceeding,
        })
