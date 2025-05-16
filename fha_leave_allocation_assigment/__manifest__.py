# -*- coding: utf-8 -*-
{
    'name': "Fecha de validación en ausencias",

    'summary': """
        Módulo para poder editar el campo de periodo de validez
        cuando la solicitud de asignación esté en estado 'enviar'
        y añadirlo en la vista hr_holidays.hr_leave_allocation_view_form_dashboard""",

    'description': """
        Módulo para poder editar el campo de periodo de validez
        cuando la solicitud de asignación esté en estado 'enviar' 
        y añadirlo en la vista hr_holidays.hr_leave_allocation_view_form_dashboard
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Asistencias',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_holidays'],

    # always loaded
    'data': [
        'views/views_leave_assigments.xml'
    ]
}
