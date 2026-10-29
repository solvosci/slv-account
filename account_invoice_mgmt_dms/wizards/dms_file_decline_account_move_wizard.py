# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, _


class AccountMoveDmsFileWizard(models.TransientModel):
    _name = 'dms.file.decline.account.move.wizard'
    _description = 'dms.file.decline.account.move.wizard'

    dms_file_id = fields.Many2one('dms.file')
    reason = fields.Char()

    def decline_account_move(self):
        self.dms_file_id.state_account_move = 'declined'
        self.dms_file_id.decline_reason = self.reason
        self.dms_file_id.account_move_id.message_post(
            body=_("Decline Invoice, reason: %s") % (self.reason)
        )
