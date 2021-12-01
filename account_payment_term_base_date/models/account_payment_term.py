# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    def compute(self, value, date_ref=False, currency=None):
        new_date_ref = self.env.context.get("custom_date_ref", date_ref)
        return super().compute(value, date_ref=new_date_ref, currency=currency)
