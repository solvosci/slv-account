# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    expected_payment_date = fields.Date()
