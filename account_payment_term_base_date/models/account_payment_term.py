# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    def _compute_terms(
        self,
        date_ref,
        currency,
        company,
        tax_amount,
        tax_amount_currency,
        sign,
        untaxed_amount,
        untaxed_amount_currency,
        cash_rounding=None,
    ):
        new_date_ref = self.env.context.get("custom_date_ref", date_ref)
        return super()._compute_terms(
            date_ref=new_date_ref,
            currency=currency,
            company=company,
            tax_amount=tax_amount,
            tax_amount_currency=tax_amount_currency,
            sign=sign,
            untaxed_amount=untaxed_amount,
            untaxed_amount_currency=untaxed_amount_currency,
            cash_rounding=cash_rounding
        )
