# Copyright 2025 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'S6R Purchase Order Invoiced Forced Qty',
    'version': '19.0.1.0.0',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "This module allows to force the invoiced quantity on Purchase Orders",
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': [
        'sale',
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module allows to force the invoiced quantity on Purchase Orders,
it is useful in customer data import scenarios where the historical supplier invoices are not imported.
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'views/purchase_order_views.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
