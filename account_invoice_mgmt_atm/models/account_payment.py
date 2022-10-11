# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, _


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    payment_ATM_id = fields.Char()

    _sql_constraints = [(
        'payment_ATM_id_unique',
        'unique(payment_ATM_id)',
        _('The payment ATM must be unique!')
    )]
