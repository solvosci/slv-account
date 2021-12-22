# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Invoice - Partner Category",
    "summary": """
        Adds partner categories for invoices, so it's possible
        to filter and group by them
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account"],
    "data": [
        "views/account_move_views.xml",
    ],
    'installable': True,
}
