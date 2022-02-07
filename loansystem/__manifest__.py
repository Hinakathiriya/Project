{
    'name': 'Loan Tracking System',
    'category' : 'Sales',
    'application' : True,
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/loan_tracking_views.xml',
        'views/loan_tracking_manus.xml',
        'wizard/loan_wizard_views.xml',
    ],


}
