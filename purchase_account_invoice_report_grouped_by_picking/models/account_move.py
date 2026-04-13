# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from collections import OrderedDict

from odoo import models
from odoo.tools import float_round

class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_signed_quantity_done(self, invoice_line, move, sign):
        if not self.picking_ids.purchase_id:
            return super()._get_signed_quantity_done(invoice_line, move, sign)

        if move.location_dest_id.usage == "internal":
            return move.quantity * sign

        if move.location_id.usage == "internal":
            return -move.quantity * sign

        return 0

    def lines_grouped_by_picking(self):
        """This prepares a data structure for printing the invoice report
        grouped by pickings.
        This method is fully overwritten from
        account_invoice_report_grouped_by_picking addon
        """
        if not self.picking_ids.purchase_id:
            return super().lines_grouped_by_picking()

        self.ensure_one()
        picking_dict = {}
        lines_dict = {}
        picking_obj = self.env["stock.picking"]

        sign = (
            -1.0
            if self.move_type == "out_refund"
            and (
                not self.reversed_entry_id
                or self.reversed_entry_id.picking_ids != self.picking_ids
            )
            else 1.0
        )

        po_dict = {p.purchase_id: p for p in self.picking_ids if p.purchase_id}

        previous_section = previous_note = False
        last_section_notes = []
        sorted_lines = self._get_grouped_by_picking_sorted_lines()
        for line in sorted_lines:

            if line.display_type in ["line_section", "line_note"]:
                if line.display_type == "line_section":
                    previous_section = line
                else:
                    previous_note = line
                last_section_notes.append(
                    {
                        "picking": picking_obj,
                        "line": line,
                        "qty": 0.0,
                        "is_last_section_notes": True,
                    }
                )
                continue

            last_section_notes = []
            has_returned_qty = False
            remaining_qty = line.quantity

            for move in line.move_line_ids:
                key = (move.picking_id, line)
                self._process_section_note_lines_grouped(
                    previous_section, previous_note, picking_dict, move.picking_id
                )
                qty = self._get_signed_quantity_done(line, move, sign)
                picking_dict[key] = picking_dict.get(key, 0.0) + qty
                remaining_qty -= qty
                if move.location_id.usage == "supplier":
                    has_returned_qty = True

            if not line.move_line_ids and line.purchase_line_id:
                for po_line in line.purchase_line_id:
                    picking = po_dict.get(po_line.order_id)
                    if picking:
                        key = (picking, line)
                        self._process_section_note_lines_grouped(
                            previous_section, previous_note, picking_dict, picking
                        )
                        qty = min(po_line.product_qty, remaining_qty)
                        picking_dict[key] = picking_dict.get(key, 0.0) + qty
                        remaining_qty -= qty

            elif not line.move_line_ids and not line.purchase_line_id:
                key = (picking_obj, line)
                self._process_section_note_lines_grouped(
                    previous_section, previous_note, lines_dict
                )
                qty = line.quantity
                picking_dict[key] = picking_dict.get(key, 0.0) + qty
                remaining_qty -= qty

            remaining_qty = float_round(
                remaining_qty,
                precision_rounding=line.product_id.uom_id.rounding or 0.01,
            )
            if (
                self.move_type == "in_refund"
                and not has_returned_qty
                and remaining_qty
                and line.product_id.type != "service"
                and picking_dict
            ):
                remaining_qty = 0.0
                for key in picking_dict:
                    picking_dict[key] = abs(picking_dict[key])
            if remaining_qty:
                self._process_section_note_lines_grouped(
                    previous_section, previous_note, lines_dict
                )
                lines_dict[line] = remaining_qty
        no_picking = [
            {"picking": picking_obj, "line": key, "quantity": value}
            for key, value in lines_dict.items()
        ]
        with_picking = [
            {"picking": key[0], "line": key[1], "quantity": value}
            for key, value in picking_dict.items()
        ]
        return no_picking + self._sort_grouped_lines(with_picking + last_section_notes)
