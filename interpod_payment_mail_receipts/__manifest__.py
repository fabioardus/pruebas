# -*- coding: utf-8 -*-
{
    'name': "interpod_payment_mail_receipts",

    'summary': """
       TDT Multiple Payment Mail Receipts 
    """,

    'description': """
        Send multiple payment mail recepits
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/multiple_payment.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'data/demo.xml',
    ],
    'license': 'OPL-1',
}
