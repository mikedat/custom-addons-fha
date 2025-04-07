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
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_timesheet'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/hr_timesheets_chief_department_views_views.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
