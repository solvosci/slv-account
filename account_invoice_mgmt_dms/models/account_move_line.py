# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    state_complete_proceesing = fields.Selection(related='move_id.state_complete_proceesing')
