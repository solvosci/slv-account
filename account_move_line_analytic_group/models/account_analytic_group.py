# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class AccountAnalyticGroup(models.Model):
    _inherit = "account.analytic.group"

    root_id = fields.Many2one(
        comodel_name="account.analytic.group",
        compute="_compute_root_id",
        readonly=True,
        store=True,
        string="Root Category",
        help="Indicates the root category for this category,"
        " or the category itself if has no parents",
    )

    @api.depends("parent_path")
    def _compute_root_id(self):
        for category in self:
            root_string = category.parent_path.split("/")[0]
            category.root_id = self.browse(int(root_string))
