# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Line Refund To Invoice Qty Force",
    "summary": """
        This module forces the quantity in the purchases order to never be subtracted.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Purchases",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["purchase_line_refund_to_invoice_qty"],
    "data": [
        "views/account_move_views.xml",
        "wizards/account_move_reversal_view.xml",
    ],
}
