# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade
import logging

logger = logging.getLogger(__name__)
logger.info(
    "Creating columns: account_move_line."
)

def pre_init_hook(cr):
    openupgrade.logged_query(
        cr, "ALTER TABLE account_move_line ADD COLUMN IF NOT EXISTS analytic_account_group_id INT"
    )
    openupgrade.logged_query(
        cr,
        """
            UPDATE account_move_line
            SET analytic_account_group_id = COALESCE(subquery.group_id, NULL)
            FROM (
                SELECT aml.analytic_account_id, analytic_account.group_id
                FROM account_move_line aml
                LEFT JOIN account_analytic_account analytic_account
                ON aml.analytic_account_id = analytic_account.id
            ) AS subquery
            WHERE account_move_line.analytic_account_id = subquery.analytic_account_id;
        """,
    )
    logger.info("Successfully updated account_move_line table")
