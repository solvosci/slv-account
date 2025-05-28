# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Intrastat Product Extra Uom Category",
    "summary": """
        When generating reports for export to Intrastat if the unit of measure category is length,
        the weight will be calculated multiplying the quantity by the weight of the product.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/solvosci/slv-account",
    "depends": ["intrastat_product"],
    "installable": True,
}
