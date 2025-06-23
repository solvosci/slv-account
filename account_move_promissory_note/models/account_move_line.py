# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def remove_move_reconcile(self):
        invoice_ids = self.payment_id.reconciled_invoice_ids
        super(AccountMoveLine, self).remove_move_reconcile()
        if invoice_ids:
            invoice_ids._calculate_payment_ids()
