# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    purchase_date_origin = fields.Datetime(compute="_compute_purchase_date_origin", compute_sudo=True)

    @api.depends('invoice_line_ids.purchase_line_id.order_id.date_order')
    def _compute_purchase_date_origin(self):
        for record in self:
            purchases = record.invoice_line_ids.mapped("purchase_line_id.order_id")
            record.purchase_date_origin = False
            if len(purchases) > 1:
                record.purchase_date_origin = min(purchases.mapped("date_order"))
            elif len(purchases) == 1:
                record.purchase_date_origin = purchases.date_order
