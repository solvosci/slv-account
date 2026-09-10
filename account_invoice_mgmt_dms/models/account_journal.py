# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    skip_invoice_publish_validator = fields.Boolean()
