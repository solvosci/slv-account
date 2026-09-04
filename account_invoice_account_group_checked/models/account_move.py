# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    has_account_checked_group = fields.Boolean(
        string='Has Account Checked Group',
        compute='_compute_has_account_checked_group',
        store=True,
        copy=False,
        help='True if at least one invoice line uses an account belonging '
             'to an account group flagged as "Will Check Invoice".',
    )

    # NOTE: 'will_check_invoice' is intentionally NOT listed as a dependency
    # here. If it were, changing that flag on an account.group would make
    # Odoo's compute engine automatically recompute this field on every
    # single invoice in the database that uses an account of that group,
    # regardless of its state (draft, posted, cancelled...). That kind of
    # mass recomputation/write is exactly what we want to avoid.
    #
    # Instead:
    # - This field is recomputed automatically only when an invoice's own
    #   lines/accounts change (normal editing of a draft invoice).
    # - When 'will_check_invoice' changes on an account.group, a targeted,
    #   draft-only recomputation is triggered explicitly from
    #   AccountGroup.write() (see account_group.py), instead of relying on
    #   the automatic dependency graph.
    @api.depends(
        'invoice_line_ids.account_id',
        'invoice_line_ids.account_id.group_id',
    )
    def _compute_has_account_checked_group(self):
        for move in self:
            # Only draft invoices are (re)evaluated. Posted or cancelled
            # invoices keep whatever value they already had, so that
            # toggling a group's flag never rewrites historical invoices.
            if move.state != 'draft':
                move.has_account_checked_group = move.has_account_checked_group
                continue
            move.has_account_checked_group = any(
                line.account_id.group_id.will_check_invoice
                for line in move.invoice_line_ids
                if line.account_id and line.account_id.group_id
            )
