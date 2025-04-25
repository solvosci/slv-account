# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_source_on_invoice_reports = fields.Boolean(string="Source", implied_group="account_invoice_report_hide_header_data.group_source_on_invoice_report")
    group_reference_on_invoice_reports = fields.Boolean(string="Reference", implied_group="account_invoice_report_hide_header_data.group_reference_on_invoice_report")
