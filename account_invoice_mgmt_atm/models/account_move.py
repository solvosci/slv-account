# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, api
import hashlib


class AccountMove(models.Model):
    _inherit = 'account.move'

    encrypted_name = fields.Char(compute='_compute_encrypted_name', store=True)
    encrypted_name_lower = fields.Char(compute='_compute_encrypted_name', store=True)
    atm_invoice = fields.Boolean()

    @api.depends('name')
    def _compute_encrypted_name(self):
        for record in self.filtered(lambda x: x.name):
            record.encrypted_name = hashlib.sha1(record.name.encode()).hexdigest()
            record.encrypted_name_lower = '%s %s' % (record.name, record.encrypted_name[0:8])

class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    def _compute_terms(
        self,
        date_ref,
        currency,
        company,
        tax_amount,
        tax_amount_currency,
        sign,
        untaxed_amount,
        untaxed_amount_currency,
        cash_rounding=None,
    ):
        return super(AccountPaymentTerm, self)._compute_terms(date_ref,
        currency,
        company,
        tax_amount,
        tax_amount_currency,
        sign,
        untaxed_amount,
        untaxed_amount_currency,
        False)