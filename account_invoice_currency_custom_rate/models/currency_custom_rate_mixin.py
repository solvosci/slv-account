# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (http://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, api, models


class CurrencyCustomRateMixin(models.AbstractModel):
    _name = "currency.custom.rate.mixin"
    _description = "Currency Custom Rate Mixin"

    custom_rate = fields.Float(
        digits=(12, 6),
        default=1,
        help="Custom currency rate for invoices.\n"
             "Used to convert between document currency and company currency."
    )
    is_custom_rate = fields.Boolean(string="Apply Custom Rate")

    custom_rate_enabled_visible = fields.Boolean(
        string="Is 'Apply Custom Currency Rate' visible",
        compute="_compute_custom_rate_enabled_visible",
    )

    @api.depends("state", "currency_id", "company_id")
    def _compute_custom_rate_enabled_visible(self):
        records = self.browse([])
        if self.env.user.has_group("account.group_account_manager"):
            records = self.filtered(
                lambda rec: (
                    rec.state not in ["draft", "done"]
                    and rec.currency_id != rec.company_id.currency_id
                )
            )
        if records:
            records.custom_rate_enabled_visible = True
        (self - records).custom_rate_enabled_visible = False

    def _prepare_invoice_custom_rate_vals(self):
        """Valores comunes para facturas"""
        if self.is_custom_rate:
            return {
                "custom_rate": self.custom_rate,
                "is_custom_rate": self.is_custom_rate,
            }
        return {}
