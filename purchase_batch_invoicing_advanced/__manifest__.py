# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Batch Invoicing Advanced",
    "summary": """
        Adds restriction when grouping by vendor with
        different journals and add your default billing journal.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Purchases",
    "website": "https://github.com/solvosci/slv-account",
    "depends": [
        "purchase_batch_invoicing",
        "purchase_order_type_advanced"
    ],
    "data": [
        "views/purchase_batch_invoicing_advanced.xml"
    ],
    'installable': True,
}
