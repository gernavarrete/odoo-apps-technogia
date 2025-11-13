{
    "name": "Cajero",
    "summary": "Gestión asistida de cajeros para registrar cobros de órdenes e imprimir documentos",
    "version": "18.0.1.0.0",
    "category": "Accounting/Point of Sale",
    "author": "Technogia",
    "website": "https://www.technogia.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "mail",
        "sale_management",
        "account",
        "hr",
        "point_of_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/cajero_menus.xml",
        "views/cajero_session_views.xml",
        "views/cajero_order_views.xml",
        "views/res_config_settings_views.xml",
        "wizard/cajero_payment_wizard_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "cajero/static/src/scss/dashboard.scss",
        ],
    },
    "images": ["static/description/icon.svg"],
    "application": True,
    "installable": True,
}
