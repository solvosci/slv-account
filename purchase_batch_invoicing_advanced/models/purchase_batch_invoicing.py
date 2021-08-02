# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, _
from odoo.exceptions import UserError


class PurchaseBatchInvoicing(models.TransientModel):
    _inherit = 'purchase.batch_invoicing'

    def grouped_purchase_orders(self):
        res = super().grouped_purchase_orders()
        for record in res:
            if len(record.mapped('order_type')) > 1:
                raise UserError(_('Selected purchase orders within the same group contain different order types.'))
            yield record

    def _prepare_batch_invoice_vals(self, partner):
        res = super()._prepare_batch_invoice_vals(partner)
        pos = self.grouped_purchase_orders()
        for purchase_order in pos:
            if purchase_order.partner_id == partner:
                res['purchase_type_id'] = purchase_order.order_type.id
                if purchase_order.order_type.journal_id:
                    res['journal_id'] = purchase_order.order_type.journal_id.id
                break
        return res
