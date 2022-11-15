# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Partner Payment Term Selection",
    "summary": """
        Remove selection widget of Payment Term and Supplier Payment Term in Partner maintenance.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account"],
    "data": [
        "views/partner_views.xml",
    ],
    'installable': True,
}
