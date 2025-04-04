# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    secondary_uom_id = fields.Many2one(
        comodel_name="product.secondary.unit",
        compute="_compute_secondary_uom_id",
    )

    secondary_uom_qty = fields.Float(
        compute="_compute_secondary_uom_id",
        digits="Product Unit of Measure"
    )

    @api.depends('product_id.sale_secondary_uom_id', 'product_id.sale_secondary_uom_id.factor' ,'sale_line_ids.secondary_uom_id')
    def _compute_secondary_uom_id(self):
        for record in self:
            if record.sale_line_ids:
                if record.sale_line_ids[0].secondary_uom_id:
                    record.secondary_uom_id = record.sale_line_ids[0].secondary_uom_id
                else:
                    if record.product_id.sale_secondary_uom_id:
                        record.secondary_uom_id = record.product_id.sale_secondary_uom_id
                    else:
                        record.secondary_uom_id = False
            elif record.product_id.sale_secondary_uom_id:
                record.secondary_uom_id = record.product_id.sale_secondary_uom_id
            else:
                record.secondary_uom_id = False

            record.secondary_uom_qty = (
                0 if not record.secondary_uom_id
                else record.quantity / record.secondary_uom_id.factor
            )
