# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Invoice Purchase Payment Date",
    "summary": """
        New expected payment date field on purchase invoices
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": [
        "account"
    ],
    "data": [
        "views/account_move_views.xml",
    ],
    'installable': True,
}
