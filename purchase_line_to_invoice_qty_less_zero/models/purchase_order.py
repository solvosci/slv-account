# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models
from odoo.tools import float_compare


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _get_invoiced(self):
        """
        For us, having more quantity invoiced tan "to invoice" (purchase or
        picking qty) it's not a problem, we're fully invoiced
        """
        super()._get_invoiced()
        prec = self.env["decimal.precision"].precision_get(
            "Product Unit of Measure"
        )
        for order in self.filtered(lambda x: x.invoice_status == "to invoice"):
            if all(
                float_compare(line.qty_to_invoice, 0.0, precision_digits=prec) <= 0
                for line in order.order_line.filtered(lambda l: not l.display_type)
            ) and order.invoice_ids:
                order.invoice_status = "invoiced"
