# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def print_account_move_80mm(self):
        self.ensure_one()
        paper_format = self.env.ref("account_move_report_80mm.account_move_ticket")
        items = self.invoice_line_ids
        paper_format.page_height = 120 + (len(items) * 11)
        return self.env.ref("account_move_report_80mm.action_account_move_pdf").report_action(self)
