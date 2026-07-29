Sometimes, knowing that an invoice has lines with accounts belonging to
certain account groups is needed.

This addon achieves it in three steps:
* For desired account group, set "Will Check Invoice" flag.
* At this moment, every current and future invoice at draft state that have
  at least one account involved for this group, will be marked ("Has Account
  Checked Group" flag).
* Invoices that have this flag (or not) can be easily located using filters
  currently available at invoices search views.

When an account group is set, those invoices that are not at draft state won't
be changed, in order to preserve invoice integrity and system overload. If we
want to be checked, it must be achived outside this application.
