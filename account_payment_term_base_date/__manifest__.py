# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Payment Term Base Date",
    "summary": """
        Enables using a base date for payment computation.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.2.0.0",
    'category': "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account_payment_term_extension"],
    "data": [
        "views/account_move_views.xml",
    ],
    'installable': True,
}
