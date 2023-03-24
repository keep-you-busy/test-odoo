# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Test',
    'version': '1.0.0',
    'category': 'Sales',
    'author': 'Odoo Solution',
    'summary': 'Test internal machinery',
    'description': """
This module is a test module based by sale_management module in odoo.
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
