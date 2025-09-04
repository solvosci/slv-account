# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_action_move_out_invoice_type_group_evaluation(self):
        return self._restrict_invoice_action("account.action_move_out_invoice_type")

    def _get_action_move_out_refund_type_group_evaluation(self):
        return self._restrict_invoice_action("account.action_move_out_refund_type")

    def _get_action_move_in_invoice_type_group_evaluation(self):
        return self._restrict_invoice_action("account.action_move_in_invoice_type")

    def _get_action_move_in_refund_type_group_evaluation(self):
        return self._restrict_invoice_action("account.action_move_in_refund_type")

    def _get_action_move_journal_line_group_evaluation(self):
        return self._restrict_invoice_action("account.action_move_journal_line")

    def _get_action_account_moves_all_group_evaluation(self):
        return self._restrict_invoice_action("account.action_account_moves_all")

    def _get_action_move_out_receipt_type_group_evaluation(self):
        return self._restrict_invoice_action("account.action_move_out_receipt_type")

    def _get_action_move_in_receipt_type_group_evaluation(self):
        return self._restrict_invoice_action("account.action_move_in_receipt_type")

    def _restrict_invoice_action(self, action_xmlid):
        action = self.env["ir.actions.act_window"]._for_xml_id(action_xmlid)
        allow = self.env.user.has_group('account.group_account_invoice')
        ctx = action.get('context') or {}
        if isinstance(ctx, str):
            ctx = eval(ctx)
        ctx.update({'create': allow, 'edit': allow, 'delete': allow})
        action['context'] = ctx
        return action
