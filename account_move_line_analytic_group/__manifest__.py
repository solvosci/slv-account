# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Move Line Filter by Analytic Group",
    "summary": """
        Filter and regroup Account Move Lines by Analytic Account group
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    'category': "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account"],
    "data": [
        "views/account_move_line_views.xml"
    ],
    'installable': True,
    'pre_init_hook': 'pre_init_hook'
}
