from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    cajero_cashbox_name = fields.Char(string="Nombre de la caja")
    cajero_payment_method_ids = fields.Many2many(
        comodel_name="account.journal",
        relation="company_cajero_payment_rel",
        column1="company_id",
        column2="journal_id",
        string="Métodos de pago del cajero",
        domain="[('type', 'in', ('cash', 'bank'))]",
    )
    cajero_cash_rounding_method_id = fields.Many2one(
        "account.cash.rounding",
        string="Redondeo de efectivo",
        help="Método de redondeo aplicado a los pagos en efectivo del cajero.",
    )
    cajero_login_as_employee = fields.Boolean(string="Iniciar sesión como empleado")
    cajero_allow_employee_switch = fields.Boolean(string="Permitir cambiar de empleado")
    cajero_basic_permissions = fields.Selection(
        selection=[
            ("restricted", "Permisos básicos"),
            ("standard", "Permisos estándar"),
        ],
        default="standard",
        string="Nivel básico",
    )
    cajero_advanced_permissions = fields.Selection(
        selection=[
            ("none", "Sin permisos avanzados"),
            ("full", "Permisos avanzados"),
        ],
        default="none",
        string="Permisos avanzados",
    )
    cajero_default_tax_id = fields.Many2one("account.tax", string="Impuesto de ventas predeterminado")
    cajero_temp_account_id = fields.Many2one(
        "account.account", string="Cuenta temporal predeterminada"
    )
    cajero_default_order_journal_id = fields.Many2one(
        "account.journal",
        string="Diario predeterminado para órdenes",
        domain="[('type', '=', 'sale')]",
    )
    cajero_default_invoice_journal_id = fields.Many2one(
        "account.journal",
        string="Diario predeterminado para facturas",
        domain="[('type', '=', 'sale')]",
    )
    cajero_auto_invoice = fields.Boolean(string="Autofacturación")
    cajero_print_portal_info = fields.Boolean(
        string="Imprimir información del portal en recibos",
        help="Incluye la URL del portal del cliente en la impresión del recibo.",
    )
    cajero_send_receipt_whatsapp = fields.Boolean(string="Enviar recibos por WhatsApp")
    cajero_foreign_currency_journal_id = fields.Many2one(
        "account.journal",
        string="Diario de cobro en moneda extranjera",
        domain="[('type', 'in', ('cash', 'bank'))]",
    )
    cajero_local_currency_journal_id = fields.Many2one(
        "account.journal",
        string="Diario de cobro en moneda local",
        domain="[('type', 'in', ('cash', 'bank'))]",
    )
