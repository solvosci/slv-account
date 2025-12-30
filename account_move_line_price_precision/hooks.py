# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

def uninstall_hook(env):
    precision = env.ref('account_move_line_price_precision.product_price_account_move_line', raise_if_not_found=False)
    precision.unlink()
