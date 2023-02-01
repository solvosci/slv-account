# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Line Refund To Invoice Qty Force",
    "summary": """
        This module forces the quantity in the sales order to never be subtracted.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sales",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["sale_line_refund_to_invoice_qty"],
    "data": [
        "views/account_move_views.xml",
        "wizards/account_move_reversal_view.xml",
    ],
}
