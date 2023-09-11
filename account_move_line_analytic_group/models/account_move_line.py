# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    analytic_account_group_id = fields.Many2one(
        'account.analytic.group',
        related='analytic_account_id.group_id',
        string='Analytic Account Group',
        readonly=True,
        store=True)

    analytic_account_group_root_id = fields.Many2one(
        'account.analytic.group',
        related='analytic_account_id.group_id.root_id',
        string='Analytic Account Root Group',
        readonly=True,
        store=True)
