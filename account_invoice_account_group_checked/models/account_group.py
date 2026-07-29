# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models


class AccountGroup(models.Model):
    _inherit = 'account.group'

    will_check_invoice = fields.Boolean(
        string='Will Check Invoice',
        default=False,
        help='If checked, any invoice that has a line using an account '
             'belonging to this group will be flagged through the '
             '"Has Account Checked Group" field on the invoice.',
    )

    def write(self, vals):
        res = super().write(vals)
        if 'will_check_invoice' in vals:
            self._recompute_draft_invoices_checked_group()
        return res

    def _recompute_draft_invoices_checked_group(self):
        """Manually recompute 'has_account_checked_group' on invoices, but
        only for invoices that are still in draft state.

        This is called explicitly instead of listing 'will_check_invoice'
        as a dependency of the compute method on account.move, precisely
        to avoid Odoo automatically recomputing (and potentially
        rewriting) that field on every invoice in the database - including
        posted and cancelled ones - every time this flag is toggled.
        """
        move_lines = self.env['account.move.line'].search([
            ('account_id.group_id', 'in', self.ids),
            ('move_id.state', '=', 'draft'),
        ])
        draft_moves = move_lines.mapped('move_id')
        if draft_moves:
            draft_moves._compute_has_account_checked_group()
