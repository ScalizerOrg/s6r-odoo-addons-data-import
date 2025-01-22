from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_invoiced_forced = fields.Float(
        string="Forced Invoiced Quantity",
        help= "Qty already invoiced but not related to existing invoices in Odoo (for history data import purposes)",
        digits='Product Unit of Measure')

    untaxed_amount_invoiced_forced = fields.Monetary(
        string="Forced Invoiced Amount",
        help="Amount already invoiced but not related to existing invoices in Odoo (for history data import purposes).\
        If this field is left blank, the pre-existing amount will not be taken in consideration when calculating the \
        total invoiced amount for the sale order. Therefore, reports relating to this sale order will be false."
    )

    @api.depends('qty_invoiced_forced')
    def _compute_qty_invoiced(self):
        super()._compute_qty_invoiced()
        for line in self:
            line.qty_invoiced += line.qty_invoiced_forced
        return

    @api.depends('untaxed_amount_invoiced_forced')
    def _compute_untaxed_amount_invoiced(self):
        super()._compute_untaxed_amount_invoiced()
        for line in self:
            line.untaxed_amount_invoiced += line.untaxed_amount_invoiced_forced
        return
