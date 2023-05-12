# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields, _
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    invoice_count = fields.Integer(compute="_invoice_purchase_order_length")

    def generate_invoice_purchase_report(self):
        for line in self.invoice_ids.filtered(lambda x: x.state == 'posted' and x.atm_invoice):
            return line.action_invoice_print()

    def _invoice_purchase_order_length(self):
        for record in self:
            record.invoice_count = len(record.invoice_ids.filtered(lambda x: x.state == 'posted' and x.atm_invoice))

    def create_atm_account_move(self):
        result = self.action_view_invoice()
        result["context"]["default_atm_invoice"] = True
        if self.amount_total >= 3000:
            raise ValidationError(_("Cannot create an invoice for cashier if the amount is greater than 3000"))
        if self.amount_total < 1000:
            result["context"]["default_invoice_cash_rounding_id"] = self.env.ref('account_invoice_mgmt_atm.account_cash_rounding_default').id
        return result
