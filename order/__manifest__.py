# -*- coding: utf-8 -*-
{
    'name': "Order Management (SDNANAS)",
    'summary': 'Module Odoo untuk melakukan pemesanan dan pengelolaan pemesanan',
    'description': 'Module Odoo untuk melakukan pemesanan barang, oleh siapa, tanggal, status, dan harga',
    'sequence': -100,
    'author': "SDNANAS",
    'category': 'Management',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/order_menus.xml',
        'views/order_trees.xml',
        'views/order_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
