# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Move Autocomplete Button Filter",
    "summary": """
         Change autocomplete button filter to get only purchase orders
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    'category': "Accounting",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["purchase"],
    "data": [
        "views/account_move_views.xml",
    ],
    'installable': True,
}
