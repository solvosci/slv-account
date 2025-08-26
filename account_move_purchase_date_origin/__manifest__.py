# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Move Purchase Date Origin",
    "summary": """
        Show the ‘original purchase date’ in the supplier invoice views
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["purchase"],
    "data": [
        "views/account_move_views.xml",
    ],
    'installable': True,
}
