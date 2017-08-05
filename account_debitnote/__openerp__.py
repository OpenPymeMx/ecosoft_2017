# -*- coding: utf-8 -*-

{
    'name': 'Invoice Debit Note',
    'version': '1.0.0',
    'author': 'OpenPyme, Ecosoft',
    'summary': 'Create Debit Note from Invoice',
    'description': """
Use the similar concept as Refund. Debit Note is in
fact Invoice with reference to previous invoice.
It will be used in every way the same as Invoice.
New type of journal has been created,
* sale_debitnote
* purchase_debitnote
Make sure the new Journal has been created for them (manually).
    """,
    'category': 'Accounting',
    'website': 'http://www.openpyme.mx',
    'images': [],
    'depends': [
        'account',
        'account_refund_linked_invoice',
    ],
    'demo': [],
    'data': [
        'wizard/account_debitnote_view.xml',
        'security/ir.model.access.csv',
        'views/account_invoice_view.xml',
        'data/account_data.xml',
    ],
    'test': [
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}
