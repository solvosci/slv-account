# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_create_invoice(self):
        res = super(PurchaseOrder, self).action_create_invoice()

        if len(self.mapped('order_type')) > 1:
            raise UserError(_('Selected purchase orders within the same group contain different order types.'))
        for move in self:
            purchase_orders = self.filtered(lambda po: po.partner_id == move.partner_id)
            if purchase_orders:
                order_type = purchase_orders[0].order_type
                res['purchase_type_id'] = order_type.id
                if order_type.journal_id:
                    res['journal_id'] = order_type.journal_id.id
        return res
