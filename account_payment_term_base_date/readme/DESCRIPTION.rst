Enables using a base date for payment computation.

The new base date is initially set with Invoice Date, or today, as Odoo does.
Once set, this date (that is always editable) will be used in due dates 
calculations, instead of Invoice Date.

This addon depends on OCA's `account_payment_term_extension <https://github.com/OCA/account-payment/tree/13.0/account_payment_term_extension>`_.

Changelog:

* 13.0.1.0.0 - Initial version, only depending of standard payment terms.
* 13.0.2.0.0 - Changed to ``account_payment_term_extension`` dependency
