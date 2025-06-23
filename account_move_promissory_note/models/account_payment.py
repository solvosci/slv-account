# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def post(self):
        res = super(AccountPayment, self).post()
        active_id = self.env.context.get('active_id')
        invoice_id = self.env['account.move'].browse(active_id).exists()
        if invoice_id:
            invoice_id._calculate_payment_ids()
        return res
