# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import _, models
from odoo.exceptions import ValidationError


class DmsDirectory(models.Model):
    _inherit = "dms.directory"

    def unlink(self):
        disabled_folders = self.sudo().env["ir.model.data"].search([
            ("module", "=", "account_invoice_mgmt_dms"),
            ("model", "=", "dms.directory"),
        ]).mapped("res_id")
        not_to_delete = [
            directory.name for directory in self.filtered(
                lambda x: x.id in disabled_folders
            )
        ]
        if not_to_delete:
            raise ValidationError(
                _(
                    "Cannot delete the following directories as required for"
                    " invoice DMS management:\n- %s"
                ) % "\n- ".join(not_to_delete)
            )
        return super().unlink()
