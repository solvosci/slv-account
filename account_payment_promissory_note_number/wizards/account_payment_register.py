# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    promissory_note_number = fields.Char()

    @api.onchange("promissory_note")
    def _onchange_promissory_note_number(self):
        if not self.promissory_note:
            self.promissory_note_number = False

    def _create_payments(self):
        payments = super()._create_payments()
        if self.promissory_note_number:
            payments.write({"promissory_note_number": self.promissory_note_number})
        return payments
