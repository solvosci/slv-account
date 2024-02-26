# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_register_payment(self):
        active_ids = self.env.context.get('active_ids')
        if not active_ids:
            return ''
        # ('type', '=', 'in_invoice')
        if self.env['account.move'].browse(active_ids).filtered(lambda x: x.state_complete_proceesing in ['pending', 'declined']):
            raise ValidationError(
                    _("Must be approved before making payment")
                )
        return super(AccountPayment, self).action_register_payment()
