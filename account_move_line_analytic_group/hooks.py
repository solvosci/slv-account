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
        cr, "ALTER TABLE account_move_line ADD COLUMN IF NOT EXISTS analytic_account_group_root_id INT"
    )
    openupgrade.logged_query(
        cr, "ALTER TABLE account_analytic_group ADD COLUMN IF NOT EXISTS root_id INT"
    )
    openupgrade.logged_query(
        cr, 
        """
            UPDATE account_analytic_group aag
            SET root_id = (
                SELECT CAST(split_part(path, '/', 1) AS INTEGER)
                FROM (
                    SELECT unnest(string_to_array(aag.parent_path, '/')) AS path
                ) AS subquery
                WHERE subquery.path <> ''
                ORDER BY array_length(string_to_array(aag.parent_path, '/'), 1)
                LIMIT 1
            );
        """
    )
    openupgrade.logged_query(
        cr,
        """
            UPDATE account_move_line
            SET analytic_account_group_id = COALESCE(subquery.group_id, NULL),
                analytic_account_group_root_id = COALESCE(subquery.root_id, NULL)
            FROM (
                SELECT aml.analytic_account_id,
                    analytic_account.group_id,
                    analytic_account_group.root_id
                FROM account_move_line aml
                LEFT JOIN account_analytic_account analytic_account
                ON aml.analytic_account_id = analytic_account.id
                LEFT JOIN account_analytic_group analytic_account_group
                ON analytic_account_group.id = analytic_account.group_id
            ) AS subquery
            WHERE account_move_line.analytic_account_id = subquery.analytic_account_id;
        """,
    )
    logger.info("Successfully updated account_move_line table")
