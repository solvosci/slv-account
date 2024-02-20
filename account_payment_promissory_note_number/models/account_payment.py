# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = "account.payment"

    promissory_note_number = fields.Char()
