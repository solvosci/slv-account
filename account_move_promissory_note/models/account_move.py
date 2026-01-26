# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    promissory_note_number = fields.Char(compute='_compute_promissory_note_number', store=True)
    payment_date = fields.Date(compute='_compute_payment_date', store=True)

    @api.depends(
        'line_ids.payment_id.promissory_note_number',
        'line_ids.matched_debit_ids.debit_move_id.payment_id.promissory_note_number',
        'line_ids.matched_debit_ids.credit_move_id.payment_id.promissory_note_number',
        'line_ids.matched_credit_ids.debit_move_id.payment_id.promissory_note_number',
        'line_ids.matched_credit_ids.credit_move_id.payment_id.promissory_note_number',
    )
    def _compute_promissory_note_number(self):
        for move in self:
            payments = move._get_reconciled_payments() | move.line_ids.payment_id
            numbers = list(dict.fromkeys(payments.mapped('promissory_note_number')))
            move.promissory_note_number = ', '.join(filter(None, numbers)) or False

    @api.depends(
        'line_ids.matched_debit_ids',
        'line_ids.matched_credit_ids',
        'line_ids.payment_id.date'
    )
    def _compute_payment_date(self):
        for move in self:
            payments = move._get_reconciled_payments()
            dates = payments.mapped('date')
            move.payment_date = max(dates) if dates else False
