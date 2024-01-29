# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Account Due List Commercial Effect Account Group",
    "summary": """
        Adds new field in Account Group commercial_effect and improve action in menuitem "Payment and due list"
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.1",
    'category': "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": [
        "account_due_list",
    ],
    "data": [
        "views/account_group_views.xml",
        "views/account_move_line_views.xml",
    ],
    'installable': True,
}
