# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_document_data(self):
        res = super()._get_document_data()
        res["in"]["location_usages"].append("internal")
        return res
