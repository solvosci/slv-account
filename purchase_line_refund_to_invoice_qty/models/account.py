# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _reverse_move_vals(self, default_values, cancel=True):
        # Set the purchase_qty_to_reinvoice based on the boolean from the
        # reversal wizard
        move_vals = super(AccountMove, self)._reverse_move_vals(
            default_values, cancel=cancel
        )
        if self.env.context.get("purchase_qty_to_reinvoice", False):
            for vals in move_vals["line_ids"]:
                vals[2].update({"purchase_qty_to_reinvoice": True})
        return move_vals


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    purchase_qty_to_reinvoice = fields.Boolean(
        string="Purchase qty to reinvoice",
        help="Leave it marked if you will reinvoice the same purchase order line",
    )
