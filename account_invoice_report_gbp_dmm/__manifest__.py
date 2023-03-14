# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Acount Invoice Report - Grouped by Picking & Manual Move based Delivery Quantity",
    "summary": """
        Links Sales Invoice Grouped By Picking with Manual Destination
        Quantities on Stock Moves
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.1",
    'category': "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": [
        "account_invoice_report_grouped_by_picking",
        "sale_order_line_deliv_move_manual",
    ],
    'installable': True,
}
