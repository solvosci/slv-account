# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_unit = fields.Float(digits='Product price - for Account Move Line')
