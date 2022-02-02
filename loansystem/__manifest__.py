{
    'name': 'Loan Tracking System',
    'category' : 'Sales',
    'application' : True,
    'depends' : ['base','account','documents'],
    'data': [
        'security/ir.model.access.csv',
        'views/loan_tracking_views.xml',
        'views/loan_tracking_manus.xml',
    ],


}
