# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, api, _
import os


class DmsFile(models.Model):
    _inherit = "dms.file"

    account_move_id = fields.Many2one('account.move', string="Invoice Files")
    ocr_doc = fields.Html('Invoice Content', compute="_compute_ocr_doc", store=True, readonly=False)
    proceeding = fields.Char()
    rating = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'Hight'),
        ('3', 'Very Hight')
    ])
    note = fields.Text()
    state_account_move = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined')
    ], string="Doc State", readonly=True)
    decline_reason = fields.Char()
    complete_proceeding = fields.Boolean(default=False)

    @api.depends('account_move_id.dms_file_ids.ocr_doc')
    def _compute_ocr_doc(self):
        directory_complete_proceeding_id = self.env.ref('account_invoice_mgmt_dms.dms_directory_complete_proceeding', raise_if_not_found=False)
        for record in self:
            if directory_complete_proceeding_id and record.directory_id == directory_complete_proceeding_id:
                dms_file_purchase_invoice = record.account_move_id.dms_file_ids.filtered(lambda x: x.id != record.id)
                record.ocr_doc = dms_file_purchase_invoice.ocr_doc

    def approve_account_move(self):
        self.state_account_move = 'approved'
        self.account_move_id.message_post(
            body=_("Approve Invoice")
        )

    def decline_account_move(self):
        Wizard = self.env['dms.file.decline.account.move.wizard']
        new = Wizard.create({
            'dms_file_id': self.id,
        })
        return {
            'name': _('Decline Purchase Invoice'),
            'res_model': 'dms.file.decline.account.move.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': new.id,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
