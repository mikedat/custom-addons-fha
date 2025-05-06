# -*- coding: utf-8 -*-
{
    'name': "Permisos para DMS",

    'summary':
      """
        Módulo para añadir los permisos DMS
      """,

    'description': """
        Módulo para añadir los permisos DMS
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",
    'category': 'Document Management',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'dms'],

    # always loaded
    'data': [
        'security/ir_rules.xml'
    ],
}
