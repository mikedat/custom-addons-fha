# -*- coding: utf-8 -*-
{
    'name': "Actualización Compras",

    'summary': """
        Módulo para añadir distintas funcionalidades al módulo de compras
        """,

    'description': """
        Módulo para añadir distintas funcionalidades al módulo de compras entre las cuales están:
            - Nuevo campo para la descripción en formulario compras.
            - Nuevo campo para la valoración en campo compras.
            - Nuevas vistas para los seguidores de compras ajenas.
            - Nuevos campos para la gestión de incidencias en compras.
    """,

    'author': "Miquel de Antonio Torné",
    'website': "https://www.yourcompany.com",
    'category': 'Purchase',
    'version': '1.0',
    'depends': ['base', 'contacts', 'purchase','base_tier_validation', 'hr'],

    # always loaded
    'data': [
        'security/ir_rule.xml',
        'views/purchase_view.xml',
        'views/res_partner.xml',
        'views/followers_view.xml',
        'views/followers_action.xml',
        'views/followers_menu.xml',
    ],
}
