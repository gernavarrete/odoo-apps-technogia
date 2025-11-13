from odoo import _, fields, models


class CajeroPaymentWizard(models.TransientModel):
    _name = "cajero.payment.wizard"
    _description = "Asistente de pago para cajero"

    session_id = fields.Many2one("cajero.session", string="Sesión", required=True)
    order_id = fields.Many2one("sale.order", string="Orden de venta", required=True)
    amount = fields.Monetary(
        string="Importe a cobrar",
        currency_field="currency_id",
        required=True,
    )
    currency_id = fields.Many2one(related="order_id.currency_id", store=False)
    journal_id = fields.Many2one(
        "account.journal",
        string="Método de pago",
        domain="[('type', 'in', ('cash', 'bank'))]",
        required=True,
    )
    communication = fields.Char(string="Referencia en recibo")

    def _prepare_invoice_values(self):
        self.ensure_one()
        self.order_id._compute_invoice_status()
        if self.order_id.invoice_status == "invoiced":
            return self.order_id.invoice_ids[:1]
        invoice = self.order_id._create_invoices()
        invoice.action_post()
        return invoice[:1]

    def action_confirm(self):
        self.ensure_one()
        invoice = self._prepare_invoice_values()
        register_payments = (
            self.env["account.payment.register"]
            .with_context(active_model="account.move", active_ids=invoice.ids)
            .create(
                {
                    "journal_id": self.journal_id.id,
                    "amount": self.amount,
                    "communication": self.communication or invoice.name,
                }
            )
        )
        register_payments.action_create_payments()
        self.session_id.message_post(
            body=_("Se registró un pago de %s para %s") % (self.amount, self.order_id.name)
        )
        action = invoice.action_view_invoice()
        action["target"] = "current"
        return action
