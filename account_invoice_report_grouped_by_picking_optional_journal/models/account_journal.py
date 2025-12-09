# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class AccountJournal(models.Model):
    _inherit = "account.journal"

    show_group_by_picking_report = fields.Boolean(
        default=True,
        string="Invoice Report - Show Grouped by Picking",
        help="Leave unmarked if original Odoo behavior (not grouped) is required for invoices belonging this journal."
    )
