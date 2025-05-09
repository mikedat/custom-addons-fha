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

    'category': 'Inventory/Purchase',
    'version': '1.0',

    'depends': ['base','purchase'],

    'data': [
        'security/ir_rule.xml',
        'views/followers_action.xml',
        'views/followers_menu.xml',
        'views/followers_view.xml'
    ]
}
