# -*- coding: utf-8 -*-
{
    'name': "Dashboard para Mantenimiento",

    'summary':
         """
        Módulo para facilitar el visionado y manejo de las tareas creadas en el módulo de Mantenimiento.
        """,

    'description': 
    """
        Módulo para facilitar el visionado y manejo de las tareas creadas en el módulo de Mantenimiento.
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing/Maintenance',
    'version': '16.0.1.0.7',

    # any module necessary for this one to work correctly
    'depends': ['base','maintenance','web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/dashboard_view.xml',
        'views/dashboard_view_expired_task.xml',
        'views/dashboard_view_pending_task.xml',
        'views/dashboard_action.xml',
        'views/dashboard_menu.xml',
        'views/views.xml'
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
