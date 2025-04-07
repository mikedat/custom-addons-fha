# -*- coding: utf-8 -*-
{
    'name': "Partes de horas para jefes",

    'summary': """
        hr_timesheet_chief_department
        """,

    'description': """
    hr_timesheet_chief_department
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Timesheets',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_timesheet', 'analytic'],

    # always loaded
    "data": [
        "security/ir_rules.xml",
        "security/ir.model.access.csv",
        "views/hr_timesheets_chief_department_menu_menu.xml",
        "views/hr_timesheets_chief_department_views_views.xml",
    ],
     'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
