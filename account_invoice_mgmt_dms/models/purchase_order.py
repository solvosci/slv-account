# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    post_portal = fields.Boolean()

    def action_post_to_potal_multi(self):
        for order in self.browse(self.env.context["active_ids"]):
            order.post_portal = True
