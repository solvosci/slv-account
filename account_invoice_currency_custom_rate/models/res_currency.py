# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api


class ResCurrency(models.Model):
    _inherit = "res.currency"

    def _get_rates(self, company, date):
        """
        Inheritance to use the provided custom rate by user
        instead of the rate from odoo.
        """
        custom_rate = self.env.context.get("custom_rate")
        to_currency = self.env.context.get("to_currency")
        if custom_rate and to_currency:
            custom = {
                currency.id: custom_rate if currency == to_currency else 1.0
                for currency in self
            }
            return custom
        return super()._get_rates(company, date)
