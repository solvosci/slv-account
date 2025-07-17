# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Invoice Report Hide Header Data",
    "summary": """
        Hide header data on invoices reports like:
        - source
        - reference, this will be always shown if invoice is a refund
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.1",
    'category': "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account"],
    "data": [
        "security/account_security.xml",
        "views/res_config_settings_views.xml",
        "reports/account_invoice_template.xml",
    ],
    'installable': True,
}
