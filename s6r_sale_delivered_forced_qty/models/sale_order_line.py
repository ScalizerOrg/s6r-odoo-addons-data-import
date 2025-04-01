from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_delivered_forced = fields.Float(
        string="Forced Delivered Qty",
        help= "Qty already delivered but not related to existing stock move in Odoo (for history data import purposes)",
        digits='Product Unit of Measure',
        copy=False,
    )

    #only adds dependency
    @api.depends('qty_delivered_forced')
    def _compute_qty_to_deliver(self):
        super()._compute_qty_to_deliver()
        return

    @api.depends('qty_delivered_forced')
    def _compute_qty_delivered(self):
        super()._compute_qty_delivered()

        for line in self:
            line.qty_delivered += line.qty_delivered_forced
        return

    # when stock moves are created, quantity is computed from already existing stock moves
    # so we need to adjust this quantity depending on the qty_received_forced field.
    def _get_qty_procurement(self, previous_product_uom_qty=False):
        qty = super()._get_qty_procurement(previous_product_uom_qty)

        if self.qty_delivered_forced:
            qty += self.qty_delivered_forced
        return qty