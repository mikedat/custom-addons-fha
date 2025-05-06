# -*- coding: utf-8 -*-
{
    'name': "Permisos para seguidores de compras",

    'summary': """
       Permisos para seguidores de compras
       """,

    'description': """
        Permisos para seguidores de compras
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        'security/ir_rule.xml',
        'views/followers_action.xml',
        'views/followers_menu.xml',
        'views/followers_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
