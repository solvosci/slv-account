# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Line Refund To Invoice Qty",
    "summary": """
        Allow deciding whether refunded quantity should be considered
        as quantity to reinvoice.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Purchases",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["purchase"],
    "data": [
        "views/account_move_views.xml",
        "views/purchase_order_views.xml",
        "wizards/account_move_reversal_view.xml",
    ]
}
