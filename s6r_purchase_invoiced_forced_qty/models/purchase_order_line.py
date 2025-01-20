from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    qty_invoiced_forced = fields.Float(
        string="Forced Billed Qty",
        help= "Qty already invoiced but not related to existing supplier invoices in Odoo (for history data import purposes)",
        digits='Product Unit of Measure')


    @api.depends('invoice_lines.move_id.state', 'invoice_lines.quantity', 'qty_received', 'product_uom_qty', 'order_id.state', 'qty_invoiced_forced')
    def _compute_qty_invoiced(self):
        super()._compute_qty_invoiced()
        for line in self:
            line.qty_invoiced += line.qty_invoiced_forced
        return
