# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models
from odoo import fields

class ResCompany(models.Model):
    _inherit = "res.company"

    cash_flow_plan_max_forecast_lines = fields.Integer(
        string="Cash Flow Plan Max Forecast Lines",
        default=100,
        help="Maximum number of forecast lines a Cash Flow Plan can generate "
        "at once when using 'Generate Forecasts'.",
    )
