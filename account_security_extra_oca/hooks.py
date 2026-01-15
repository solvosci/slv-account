# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


def uninstall_hook(env):
    env.ref("account_payment_mode.account_payment_mode_menu").parent_id = env.ref("account.account_management_menu").id
