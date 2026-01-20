# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Account Payment Promissory Note Number",
    "summary": """
        Adds new field Promissoy Note Number in account payment"
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    'category': "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": [
        "account_payment_promissory_note",
    ],
    "data": [
        "views/account_payment_views.xml",
        "wizards/account_payment_register_views.xml",
    ],
    'installable': True,
}
