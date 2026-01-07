# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _commercial_fields(self):
        fields = set(super()._commercial_fields())
        fields -= {
            "property_payment_term_id",
            "property_supplier_payment_term_id",
            "supplier_payment_mode_id",
            "customer_payment_mode_id",
        }
        return list(fields)

    @api.model_create_multi
    def create(self, vals_list):
        parents = {}
        parent_ids = {vals.get("parent_id") for vals in vals_list if vals.get("parent_id")}
        if parent_ids:
            parents = {p.id: p for p in self.env["res.partner"].browse(parent_ids)}

        for vals in vals_list:
            parent_id = vals.get("parent_id")
            if not parent_id:
                continue

            parent = parents.get(parent_id)
            if not parent:
                continue

            vals.setdefault("property_payment_term_id", parent.property_payment_term_id.id)
            vals.setdefault("property_supplier_payment_term_id", parent.property_supplier_payment_term_id.id)
            vals.setdefault("customer_payment_mode_id", parent.customer_payment_mode_id.id)
            vals.setdefault("supplier_payment_mode_id", parent.supplier_payment_mode_id.id)

        return super().create(vals_list)
