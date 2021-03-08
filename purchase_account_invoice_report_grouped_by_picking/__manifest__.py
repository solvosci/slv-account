# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Invoice Grouped by Picking - extended to Purchase",
    "summary": "Print invoice lines grouped by picking, including purchase invoices",
    "version": "13.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "author": "Solvos",
    "license": "LGPL-3",
    "depends": [
        "purchase_stock_picking_invoice_link",
        "account_invoice_report_grouped_by_picking"
    ],
    "data": ["views/report_invoice.xml"],
}
