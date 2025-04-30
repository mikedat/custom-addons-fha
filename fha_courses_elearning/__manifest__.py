# -*- coding: utf-8 -*-
{
    'name': "Cursos E-Learning",

    'summary': """
        Cursos E-Learning""",

    'description': """
        Cursos E-Learning
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','website','mail','website_slides'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/courses_views.xml',
        'views/courses_menu.xml',
        'views/courses_actions.xml'
    ],
    'application': True,
}
