import logging
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    logging.getLogger('odoo.addons.account_move_promissory_note').info(
        'Create new table account_invoice_payment_rel_2')

    openupgrade.logged_query(
        env.cr,
        """
        CREATE TABLE account_invoice_payment_rel_2 (
            invoice_id INTEGER NOT NULL,
            payment_id INTEGER NOT NULL
        );
        """,
    )
    logging.getLogger('odoo.addons.account_move_promissory_note').info(
        'Initializing account_invoice_payment_rel_2 with data from account_invoice_payment_rel')

    openupgrade.logged_query(
        env.cr,
        """
        INSERT INTO account_invoice_payment_rel_2 (invoice_id, payment_id)
        SELECT invoice_id, payment_id FROM account_invoice_payment_rel;
        """,
    )
