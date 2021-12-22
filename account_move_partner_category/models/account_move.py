# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)
from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    partner_category_ids = fields.Many2many(
        related="partner_id.category_id",
    )
    partner_category_count = fields.Integer(
        compute="_compute_partner_categories",
    )
    partner_categories = fields.Char(
        compute="_compute_partner_categories",
        store=True,
        readonly=True,
        help="Technical field for partner category grouping",
    )

    @api.depends("partner_category_ids")
    def _compute_partner_categories(self):
        for move in self:
            move.partner_categories = (
                ", ".join(move.partner_category_ids.mapped("display_name"))
                if move.partner_category_ids
                else _("Uncategorized")
            )
            move.partner_category_count = len(move.partner_category_ids)
