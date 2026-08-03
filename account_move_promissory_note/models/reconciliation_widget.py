# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, api


class AccountReconciliation(models.AbstractModel):
    _inherit = 'account.reconciliation.widget'

    @api.model
    def _process_move_lines(self, move_line_ids, new_mv_line_dicts):
        super(AccountReconciliation, self)._process_move_lines(move_line_ids, new_mv_line_dicts)
        account_move_line = self.env['account.move.line'].browse(move_line_ids)
        invoice_id = account_move_line.move_id.filtered(lambda move: move.is_invoice())
        invoice_id._calculate_payment_ids()
