# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    payment_ids = fields.Many2many('account.payment', 'account_invoice_payment_rel', 'invoice_id' , 'payment_id')
    promissory_note_number = fields.Char(compute='_compute_promissory_note_number', store=True)

    @api.depends('payment_ids.promissory_note_number')
    def _compute_promissory_note_number(self):
        for record in self:
            record.promissory_note_number = ', '.join(record.payment_ids.filtered(lambda x: x.promissory_note_number).mapped('promissory_note_number'))
