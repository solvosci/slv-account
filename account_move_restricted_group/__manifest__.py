# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Move Restricted Group",
    "summary": """
        Restrict creation, edit and delete on tree and form view in account moves
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account"],
    "data": [
        "views/account_move_view.xml"
    ],
    "installable": True,
    "uninstall_hook": "uninstall_hook",
}
