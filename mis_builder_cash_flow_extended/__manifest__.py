# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "MIS Builder Cash Flow Extended",
    "version": "17.0.1.0.0",
    'summary': 'Cash flow forecast line categories and recurrent cash flow plans.',
    "license": "AGPL-3",
    "author": "Solvos, " "Odoo Community Association (OCA)",
    "website": "https://github.com/slv/slv-account",
    "depends": ["mis_builder_cash_flow"],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/cash_flow_category_views.xml',
        'views/cash_flow_plan_views.xml',
        'views/cash_flow_forecast_line_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False
}
