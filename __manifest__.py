# -*- coding: utf-8 -*-
{
    'name': 'Accounts - 4i Accounting',
    'version': '0.1',
    'author': 'Benlever Pvt Ltd',
    'company': 'Benelever Pvt Ltd',
    'website': 'https://www.benlever.com',
    'maintainer': 'Benlever Pvt Ltd',
    'category': 'Accounting/Accounting',
    'sequence': 6,
    'summary': 'Maker Checker for Accounting Module.',
    'description': """

It gives the more flexibility to define groups who have can post entries as opposed to who can create a draft.

""",
    'depends': ['account', 'account_asset'],
    'data': [
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}
