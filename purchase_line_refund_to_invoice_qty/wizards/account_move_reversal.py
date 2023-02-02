# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models


class AccountMoveReversal(models.TransientModel):
    _inherit = "account.move.reversal"

    purchase_qty_to_reinvoice = fields.Boolean(
        string="This credit note will be reinvoiced",
        default=True,
        help="Leave it marked if you will reinvoice the same purchase order line "
        "(standard behaviour)",
    )

    def reverse_moves(self):
        return super(
            AccountMoveReversal,
            self.with_context(purchase_qty_to_reinvoice=self.purchase_qty_to_reinvoice),
        ).reverse_moves()
