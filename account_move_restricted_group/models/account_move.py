# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, api, _
from odoo.exceptions import AccessError

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def check_access_rights(self, operation, raise_exception=True):
        """ Restrict create, write, unlink operations on account.move
            to users in the 'Invoicing & Accounting' group.
        """
        user = self.env.user
        group = "account.group_account_invoice"

        # Only restrict create, write, unlink operations
        if (
            operation != "read"
            and not self.env.su
            and not user.has_group(group)
        ):
            if raise_exception:
                raise AccessError(
                    _("You do not have the necessary permissions to perform this operation.")
                )
            return False

        # If the operation is 'read' or the user has the group, proceed as normal
        return super().check_access_rights(operation=operation, raise_exception=raise_exception)
