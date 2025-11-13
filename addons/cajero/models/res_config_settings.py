from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    cajero_cashbox_name = fields.Char(related="company_id.cajero_cashbox_name", readonly=False)
    cajero_payment_method_ids = fields.Many2many(
        related="company_id.cajero_payment_method_ids",
        string="Métodos de pago",
        readonly=False,
    )
    cajero_cash_rounding_method_id = fields.Many2one(
        related="company_id.cajero_cash_rounding_method_id",
        readonly=False,
    )
    cajero_login_as_employee = fields.Boolean(related="company_id.cajero_login_as_employee", readonly=False)
    cajero_allow_employee_switch = fields.Boolean(
        related="company_id.cajero_allow_employee_switch",
        readonly=False,
    )
    cajero_basic_permissions = fields.Selection(
        related="company_id.cajero_basic_permissions",
        readonly=False,
    )
    cajero_advanced_permissions = fields.Selection(
        related="company_id.cajero_advanced_permissions",
        readonly=False,
    )
    cajero_default_tax_id = fields.Many2one(
        related="company_id.cajero_default_tax_id",
        readonly=False,
    )
    cajero_temp_account_id = fields.Many2one(
        related="company_id.cajero_temp_account_id",
        readonly=False,
    )
    cajero_default_order_journal_id = fields.Many2one(
        related="company_id.cajero_default_order_journal_id",
        readonly=False,
    )
    cajero_default_invoice_journal_id = fields.Many2one(
        related="company_id.cajero_default_invoice_journal_id",
        readonly=False,
    )
    cajero_auto_invoice = fields.Boolean(related="company_id.cajero_auto_invoice", readonly=False)
    cajero_print_portal_info = fields.Boolean(
        related="company_id.cajero_print_portal_info",
        readonly=False,
    )
    cajero_send_receipt_whatsapp = fields.Boolean(
        related="company_id.cajero_send_receipt_whatsapp",
        readonly=False,
    )
    cajero_foreign_currency_journal_id = fields.Many2one(
        related="company_id.cajero_foreign_currency_journal_id",
        readonly=False,
    )
    cajero_local_currency_journal_id = fields.Many2one(
        related="company_id.cajero_local_currency_journal_id",
        readonly=False,
    )
