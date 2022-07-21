# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    """
    Recompute field in order to propagate new values
    Only those invoices with a different commercial partner to invoice partner
    will be recomputed
    """
    # TODO Postgres code if there's too invoices
    # TODO equivalent to search([]).filtered(lambda x: x.partner_id != x.commercial_partner_id)
    #      but faster
    env["account.move"].search([
        ("partner_id.is_company", "=", False),
        ("partner_id.parent_id", "!=", False),
    ])._compute_partner_categories()
