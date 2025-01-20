from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_invoiced_forced = fields.Float(
        string="Forced Invoiced Quantity",
        help= "Qty already invoiced but not related to existing invoices in Odoo (for history data import purposes)",
        digits='Product Unit of Measure')


    @api.depends('invoice_lines.move_id.state', 'invoice_lines.quantity', 'qty_invoiced_forced')
    def _compute_qty_invoiced(self):
        super()._compute_qty_invoiced()
        for line in self:
            line.qty_invoiced += line.qty_invoiced_forced
        return
