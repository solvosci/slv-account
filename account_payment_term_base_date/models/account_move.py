# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_default_invoice_pt_base_date(self):
        """
        Inspired on _recompute_payment_terms_lines._get_payment_terms_computation_date
        method of account.move
        """
        today = fields.Date.context_today(self)
        if self.invoice_payment_term_id:
            return self.invoice_date or today
        else:
            return (
                self.invoice_date_due or self.invoice_date or today
            )

    invoice_pt_base_date = fields.Date(
        string="Due base date",
        copy=False,
        default=_get_default_invoice_pt_base_date,
    )

    @api.depends("invoice_pt_base_date")
    def _compute_needed_terms(self):
        inv_with_pt_base_date = self.filtered(lambda x: x.invoice_pt_base_date)
        for invoice in inv_with_pt_base_date:
            invoice = invoice.with_context(
                custom_date_ref=invoice.invoice_pt_base_date,
            )
            super(AccountMove, invoice)._compute_needed_terms()
        super(AccountMove, self -  inv_with_pt_base_date)._compute_needed_terms()
