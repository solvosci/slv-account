# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class AccountMove(models.Model):
    _inherit="account.move"

    def lines_grouped_by_picking(self):
        self.ensure_one()
        if not self.journal_id.show_group_by_picking_report:
            return [{"line": line, "quantity": line.quantity, "picking": None} for line in self.invoice_line_ids]

        return super().lines_grouped_by_picking()
