# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_signed_quantity_done(self, invoice_line, move, sign):
        if move.product_id.invoice_policy == "stock_move_dest":
            qty = 0
            if move.location_id.usage == "customer":
                qty = -move.qty_delivered_dest * sign
            elif move.location_dest_id.usage == "customer":
                qty = move.qty_delivered_dest * sign
        else:
            qty = super()._get_signed_quantity_done(invoice_line, move, sign)
        return qty
