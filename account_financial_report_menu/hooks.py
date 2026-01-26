# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import SUPERUSER_ID, api


def uninstall_hook(env):
    env.ref("account_financial_report.menu_oca_reports").parent_id = env.ref("account.menu_finance_reports").id
