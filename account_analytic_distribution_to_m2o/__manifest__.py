# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Analytic Distribution To M2O",
    "summary": """
        Adds back a traditional analytic account field (analytic_account_id) on journal items.
        The field is computed from the first line of Odoo's analytic distribution JSON.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    'category': "Accounting/Accounting",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ['account'],
    "data": [
        "views/account_move_views.xml",
    ],
    "installable": True,
}
