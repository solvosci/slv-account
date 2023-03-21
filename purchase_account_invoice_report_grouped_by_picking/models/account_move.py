# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from collections import OrderedDict

from odoo import models
from odoo.tools import float_is_zero


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_document_data(self):
        """
        If needed, extend or modify it
        """
        return {
            "in": {
                "type_refund": "in_refund",
                "document_id": "purchase_id",
                "location_usages": ["supplier"],
                "line_ids": "purchase_line_id",
                "sign": -1.0,
            },
            "out": {
                "type_refund": "out_refund",
                "document_id": "sale_id",
                "location_usages": ["customer"],
                "line_ids": "sale_line_ids",
                "sign": 1.0,
            },
        }

    def lines_grouped_by_picking(self):
        """This prepares a data structure for printing the invoice report
        grouped by pickings.
        This method is fully overwritten from 
        account_invoice_report_grouped_by_picking addon
        """
        self.ensure_one()
        picking_dict = OrderedDict()
        lines_dict = OrderedDict()

        document_data = self._get_document_data()

        inv_type = "in" if self.type in ("in_invoice", "in_refund", "in_receipt") else "out"        

        # Not change sign if the credit note has been created from reverse move option
        # and it has the same pickings related than the reversed invoice instead of sale
        # order invoicing process after picking reverse transfer
        sign = (
            -1.0
            if self.type == document_data[inv_type]["type_refund"]
            and (
                not self.reversed_entry_id
                or self.reversed_entry_id.picking_ids != self.picking_ids
            )
            else 1.0
        )
        sign *= document_data[inv_type]["sign"]
        # Let's get first a correspondance between pickings and sales order
        doc_dict = {x[document_data[inv_type]["document_id"]]: x for x in self.picking_ids if x[document_data[inv_type]["document_id"]]}
        # Compatibility with solvosci/slv-account/account_invoice_report_gbp_dmm
        #  without need of addons strict dependency
        selfctx = self.with_context(
            signed_quantity_done_endloc=document_data[inv_type]["location_usages"],
            signed_quantity_done_qtyfield="quantity_done" if inv_type == "in" else False,
        )
        # Now group by picking by direct link or via same SO as picking's one
        for line in self.invoice_line_ids.filtered(lambda x: not x.display_type):
            remaining_qty = line.quantity
            for move in line.move_line_ids:
                key = (move.picking_id, line)
                picking_dict.setdefault(key, 0)
                qty = selfctx._get_signed_quantity_done(line, move, sign)
                picking_dict[key] += qty
                remaining_qty -= qty
            if not line.move_line_ids and line[document_data[inv_type]["line_ids"]]:
                for so_line in line[document_data[inv_type]["line_ids"]]:
                    if doc_dict.get(so_line.order_id):
                        key = (doc_dict[so_line.order_id], line)
                        picking_dict.setdefault(key, 0)
                        qty = so_line.product_uom_qty
                        picking_dict[key] += qty
                        remaining_qty -= qty
            if not float_is_zero(
                remaining_qty,
                precision_rounding=line.product_id.uom_id.rounding or 0.01,
            ):
                lines_dict[line] = remaining_qty
        no_picking = [
            {"picking": False, "line": key, "quantity": value}
            for key, value in lines_dict.items()
        ]
        with_picking = [
            {"picking": key[0], "line": key[1], "quantity": value}
            for key, value in picking_dict.items()
        ]
        return no_picking + self._sort_grouped_lines(with_picking)
