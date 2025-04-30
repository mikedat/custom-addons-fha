# -*- coding: utf-8 -*-
{
    'name': "Permisos departamentales en compras",

    'summary': """
        Módulo para añadir permisos en la visualización de las compras
        """,

    'description': """
        Módulo para añadir permisos en la visualización de las compras
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Purchase',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','hr'],

    # always loaded
    'data': [
        'security/ir_rules.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
