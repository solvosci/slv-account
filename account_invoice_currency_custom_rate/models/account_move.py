# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, models, fields


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "currency.custom.rate.mixin"]

    def apply_custom_rate(self):
        today = fields.Date.context_today(self)
        invoices = self.filtered(lambda x: x.state == "draft").with_context(
            check_move_validity=False,
        )
        for invoice in invoices:
            invoice_date = invoice.invoice_date or today
            to_currency = invoice.currency_id
            context = {"custom_rate": invoice.custom_rate, "to_currency": to_currency}
            to_currency = invoice.currency_id.with_context(**context)
            from_currency = self.env.company.currency_id.with_context(**context)

            for line in invoice.invoice_line_ids:
                line.credit = to_currency._convert(
                    line.price_subtotal,
                    from_currency,
                    invoice.company_id,
                    invoice_date,
                )
            invoice.with_context(**context)._recompute_dynamic_lines(recompute_all_taxes=True)

    @api.onchange("date", "currency_id")
    def _onchange_currency(self):
        if not self.is_custom_rate:
            super(AccountMove, self)._onchange_currency()

    @api.model_create_multi
    def create(self, vals_list):
        rslt = super(AccountMove, self).create(vals_list)
        for i, vals in enumerate(vals_list):
            if "is_custom_rate" in vals:
                rslt[i].apply_custom_rate()
        return rslt

    @api.onchange("custom_rate")
    def _onchange_custom_rate(self):
        if self.custom_rate != 1:
            self.apply_custom_rate()
