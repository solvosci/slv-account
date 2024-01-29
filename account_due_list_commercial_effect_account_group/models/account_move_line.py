# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    commercial_effect = fields.Boolean(related='account_id.group_id.commercial_effect', store=True)
