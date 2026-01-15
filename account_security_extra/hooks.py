# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


def uninstall_hook(env):
    env.ref("account.menu_action_account_form").parent_id = env.ref("account.account_account_menu").id
    env.ref("account.menu_action_payment_term_form").parent_id = env.ref("account.account_invoicing_menu").id
