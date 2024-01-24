# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import api, models


class GeneralLedgerReport(models.AbstractModel):
    _inherit = "report.account_financial_report.general_ledger"

    @api.model
    def _recalculate_cumul_balance(
        self, move_lines, last_cumul_balance, rec_after_date_to_ids
    ):
        move_lines = sorted(move_lines, key=lambda k: (k["date"], k["entry"]))
        return super()._recalculate_cumul_balance(move_lines, last_cumul_balance, rec_after_date_to_ids)
