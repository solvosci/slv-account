# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_signed_quantity_done(self, invoice_line, move, sign):
        qty = super()._get_signed_quantity_done(invoice_line, move, sign)
        # Compatibility with solvosci/slv-account/purchase_account_invoice_report_grouped_by_picking
        #  without need of addons strict dependency
        end_locations = (
            self.env.context.get("signed_quantity_done_endloc")
            or
            ["customer"]
        )
        qty_field = (
            self.env.context.get("signed_quantity_done_qtyfield")
            or
            "qty_delivered_dest"
        )
        if move.product_id.invoice_policy == "stock_move_dest":
            if move.location_id.usage in end_locations:
                qty = -move[qty_field] * sign
            elif move.location_dest_id.usage in end_locations:
                qty = move[qty_field] * sign
        return qty
