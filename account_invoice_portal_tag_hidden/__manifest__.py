# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Invoice - Portal Tag Hidden",
    "summary": """
        Hide status tags in the invoice portal
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account_payment"],
    "data": [
        "data/account_payment.xml",
        "views/account_portal_template.xml",
    ],
    'installable': True,
}
