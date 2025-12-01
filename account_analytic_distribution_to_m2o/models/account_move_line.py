# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models
import json

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    first_analytic_account_id = fields.Many2one(
        'account.analytic.account',
        compute='_compute_first_analytic_account_id',
        index=True,
        help="Returns the first analytic account saved at analytic distribution",
        store=True
    )

    @api.depends('analytic_distribution')
    def _compute_first_analytic_account_id(self):
        for line in self:
            analytic_id = False
            if line.analytic_distribution:
                try:
                    distribution_dict = json.loads(line.analytic_distribution) if isinstance(line.analytic_distribution, str) else line.analytic_distribution

                    if distribution_dict:
                        analytic_id = int(list(distribution_dict.keys())[0])

                except (json.JSONDecodeError, ValueError):
                    pass

            line.first_analytic_account_id = analytic_id and self.env['account.analytic.account'].browse(analytic_id) or False


