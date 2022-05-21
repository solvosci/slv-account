# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Account Invoice Report Grouped By Picking and Original Formats",
    "summary": """
        Duplicates invoice report entries and makes again accessible original invoice format
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    'category': "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account_invoice_report_grouped_by_picking"],
    "data": [
        "data/ir_ui_view.xml",
        "reports/account_invoice_report.xml",
        "reports/account_invoice_report_templates.xml",
    ],
    'installable': True,
}
