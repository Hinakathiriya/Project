{
    'name': 'Loan Tracking System Extend',
    'category' : 'Sales',
    'application' : True,
    'depends' : ['base','loansystem'],
    'data': [
        'security/ir.model.access.csv',
        'views/loansystem_extend_views.xml',
        'views/loansystem_extend_manus.xml',
    ],

}
