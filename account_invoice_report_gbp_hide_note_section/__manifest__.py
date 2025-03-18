# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Account Invoice Report GBP Hide Note Section",
    "summary": """
        For grouped by picking invoice report, hides note and section lines 
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    'category': "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account_invoice_report_grouped_by_picking"],
    "data": [
        "views/report_invoice.xml"
    ],
    'installable': True,
}
