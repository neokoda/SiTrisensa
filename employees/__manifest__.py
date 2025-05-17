# -*- coding: utf-8 -*-
{
    'name': "Employees (SDNANAS)",
    'summary': 'Module Odoo untuk menyimpan data employee.',
    'description': 'Module Odoo untuk melakukan pembacaan dan modifikasi pada data employee SiTrisensa.',
    'sequence': -100,
    'author': "SDNANAS",
    'category': 'Human Resources',
    'version': '1.0',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employees_menus.xml',
        'views/employees_trees.xml',
        'views/employees_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}