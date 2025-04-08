# -*- coding: utf-8 -*-
{
    'name': "Dashboard mantenimiento",

    'summary': """
        Addon para poder administrar el módulo de mantenimiento
        """,

    'description': """
        Addon para poder administrar de manera correcta el módulo de mantenimiento
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing/Maintenance',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'maintenance'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/hr_maintenance_dashboard_actions_menu_views.xml",
        "views/hr_maintenance_dashboard_menu_action_action.xml",
        "views/hr_maintenance_dashboard_view_views.xml",
        "views/templates.xml",
        "views/views.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
