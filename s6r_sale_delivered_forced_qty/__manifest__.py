# Copyright 2025 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'S6R Sale Order Line Delivered Forced Qty',
    'version': '18.0.1.0.1',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "S6R Sale Order Line Delivered Forced Qty",
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': [
        'sale_stock',
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module allows to force the delivered quantity on Sale Order Lines,
it is useful in customer data import scenarios where the historical stock moves are not imported.
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
