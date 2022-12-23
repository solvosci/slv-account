# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Invoice Payment Ref Mandatory",
    "summary": """
         Adds required payment_reference field
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    'category': "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account"],
    "data": [
        "views/account_move_views.xml",
    ],
    'installable': True,
}
