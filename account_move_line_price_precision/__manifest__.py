# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Account Move Line Price Precision",
    "summary": """
        Adds separate decimal precision for product unit prices in account.move.line,
        allowing more decimals in accounting entries than in sales or purchase lines
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["account"],
    "data": [
        "data/decimal_precision.xml"
    ],
    "installable": True,
    "uninstall_hook": "uninstall_hook",
}
