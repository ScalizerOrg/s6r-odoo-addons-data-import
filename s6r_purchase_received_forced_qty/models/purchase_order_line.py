from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    qty_received_forced = fields.Float(
        string="Forced Received Qty",
        help= "Qty already received but not related to existing stock move in Odoo (for history data import purposes)",
        digits='Product Unit of Measure',
        copy=False,
    )

    @api.depends('qty_received_forced')
    def _compute_qty_received(self):
        super()._compute_qty_received()
        for line in self:
            line.qty_received += line.qty_received_forced
        return

    # when stock moves are created, quantity is computed from already existing stock moves
    # so we need to adjust this quantity depending on the qty_received_forced field.
    def _get_qty_procurement(self):
        qty = super()._get_qty_procurement()

        if self.qty_received_forced:
            qty += self.qty_received_forced
        return qty