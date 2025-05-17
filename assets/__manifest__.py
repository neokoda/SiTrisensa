# -*- coding: utf-8 -*-
{
    'name': "Assets Management (SDNANAS)",
    'summary': 'Module Odoo untuk menyimpan dan mengelola data aset perusahaan.',
    'description': 'Module Odoo untuk melakukan pencatatan, pembacaan, dan modifikasi data aset seperti nama, deskripsi, stok, dan harga.',
    'sequence': -100,
    'author': "SDNANAS",
    'category': 'Management',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets_menus.xml',
        'views/assets_trees.xml',
        'views/assets_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
