# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, _


class IntrastatProductDeclaration(models.Model):
    _inherit = "intrastat.product.declaration"

    def _get_weight_and_supplunits(self, inv_line, hs_code, notedict):
        source_uom = inv_line.product_uom_id
        length_uom_categ = self.env.ref("uom.uom_categ_length")

        if source_uom.category_id == length_uom_categ:
            line_qty = inv_line.quantity
            intrastat_unit_id = hs_code.intrastat_unit_id
            target_uom = intrastat_unit_id.uom_id
            product = inv_line.product_id
            weight = suppl_unit_qty = 0.0

            if not product.weight:
                line_notes = [_("Missing weight on product %s.") % product.display_name]
                self._format_line_note(inv_line, notedict, line_notes)
                return weight, suppl_unit_qty

            weight = product.weight * line_qty
            if intrastat_unit_id:
                suppl_unit_qty = source_uom._compute_quantity(line_qty, target_uom)

            return weight, suppl_unit_qty
        else:
            return super()._get_weight_and_supplunits(inv_line, hs_code, notedict)
