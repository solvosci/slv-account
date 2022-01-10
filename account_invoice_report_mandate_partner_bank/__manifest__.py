# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Invoice Report - Mandate Partner Bank",
    "summary": """
        Adds partner bank account to the Invoice Report when a
        mandate is involved
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    'category': "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account_banking_mandate"],
    "data": [
        "reports/account_invoice_template.xml",
    ],
    'installable': True,
}
