{
    "name": "Incidencias en compras",
    "summary": """Incidencias en compras""",
    "version": "16.0.1.0.0",
    "description": """Incidencias en compras""",
    "author": "Miquel de Antonio Torné",
    "company": "MyCompany",
    "category": "Purchase",
    "depends": [
        "purchase",
        "contacts",
        "base_tier_validation",
    ],
    "license": "AGPL-3",
    "data": [
        "security/ir_rule.xml",
        "views/purchase_view.xml",
        "views/res_partner.xml",
    ],
    "installable": True,
    "auto_install": True,
}
