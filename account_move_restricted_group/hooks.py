# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


def uninstall_hook(env):
    # Original contexts of each action
    action_context_map = {
        "account.action_move_out_invoice_type": {'default_move_type': 'out_invoice'},
        "account.action_move_out_refund_type": {'default_move_type': 'out_refund', 'display_account_trust': True},
        "account.action_move_in_invoice_type": {'default_move_type': 'in_invoice', 'display_account_trust': True},
        "account.action_move_in_refund_type": {'default_move_type': 'in_refund'},
        "account.action_move_journal_line": {'default_move_type': 'entry', 'search_default_posted': 1, 'view_no_maturity': True},
        "account.action_account_moves_all": {'journal_type': 'general', 'search_default_posted': 1},
        "account.action_move_out_receipt_type": {'default_move_type': 'out_receipt'},
        "account.action_move_in_receipt_type": {'default_move_type': 'in_invoice', 'display_account_trust': True},
    }

    for action_xmlid, original_ctx in action_context_map.items():
        action = env.ref(action_xmlid, raise_if_not_found=False)
        if action:
            action.write({'context': original_ctx})

    # Original actions of each menu
    menu_action_map = {
        "account.menu_action_move_out_invoice_type": "account.action_move_out_invoice_type",
        "account.menu_action_move_out_refund_type": "account.action_move_out_refund_type",
        "account.menu_action_move_in_invoice_type": "account.action_move_in_invoice_type",
        "account.menu_action_move_in_refund_type": "account.action_move_in_refund_type",
        "account.menu_action_move_journal_line_form": "account.action_move_journal_line",
        "account.menu_action_account_moves_all": "account.action_account_moves_all",
        "account.menu_action_move_out_receipt_type": "account.action_move_out_receipt_type",
        "account.menu_action_move_in_receipt_type": "account.action_move_in_receipt_type",
    }

    for menu_xmlid, action_xmlid in menu_action_map.items():
        menu = env.ref(menu_xmlid, raise_if_not_found=False)
        action = env.ref(action_xmlid, raise_if_not_found=False)
        if menu and action:
            menu.write({"action": f"{action._name},{action.id}"})