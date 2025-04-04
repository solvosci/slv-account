# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Move Report Secondary Unit",
    "summary": """
        Add the secondary unit of measure in invoice reports
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["sale_order_secondary_unit"],
    "data": [
        "report/report_invoice_document.xml"
    ],
    "installable": True,
}
