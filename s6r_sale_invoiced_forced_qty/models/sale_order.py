from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.untaxed_amount_invoiced_forced')
    def _compute_amount_to_invoice(self):
        super()._compute_amount_to_invoice()
        for order in self:
            if order.invoice_status == 'invoiced':
                # if order is fully invoiced, its amount_to_invoice has already been set to 0
                continue
            for line in order.order_line:
                ## we need to calculate the tax value for our forced invoiced amount,
                ## to use the generic method we need to convert our amount to a tax base line first
                forced_invoiced_amount_taxbaseline = line._prepare_base_line_for_taxes_computation(
                    quantity=1,
                    price_unit=line.untaxed_amount_invoiced_forced,
                    discount=0,
                )
                #calculate tax on forced amount using the account generic method
                self.env['account.tax']._add_tax_details_in_base_line(forced_invoiced_amount_taxbaseline, line.company_id)
                taxed_amount_invoiced_forced = forced_invoiced_amount_taxbaseline['tax_details']['raw_total_included_currency']

                order.amount_to_invoice -= taxed_amount_invoiced_forced
        return
