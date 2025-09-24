# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'S6R Sale Order Invoiced Forced Qty',
    'version': '18.0.1.0.3',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "This module allows to force the invoiced quantity on Sale Orders",
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': [
        'sale',
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module allows to force the invoiced quantity on Sale Orders,
it is useful in customer data import scenarios where the historical invoices are not imported.
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'views/sale_order_views.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
