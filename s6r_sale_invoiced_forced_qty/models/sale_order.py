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
                forced_invoiced_amount_taxbaseline = line._convert_to_tax_base_line_dict()
                #then change the values that we need
                forced_invoiced_amount_taxbaseline.update({
                    'quantity': 1,
                    'price_unit': line.untaxed_amount_invoiced_forced,
                    'price_subtotal' : line.untaxed_amount_invoiced_forced,
                    'discount' : 0,
                })
                #calculate tax on forced amount using the account generic method
                tax_results = self.env['account.tax'].with_company(line.company_id)._compute_taxes([
                    forced_invoiced_amount_taxbaseline
                ])
                totals = list(tax_results['totals'].values())[0]
                taxed_amount_invoiced_forced = totals['amount_tax'] + totals['amount_untaxed']

                order.amount_to_invoice -= taxed_amount_invoiced_forced
                pass
        return
