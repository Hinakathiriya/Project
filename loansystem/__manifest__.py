{
    'name': 'Loan Tracking System',
    'category' : 'Sales',
    'application' : True,
    'depends' : ['base','website','mail'],
    'data': [
        'security/loan_security.xml',
        'security/ir.model.access.csv',
        'views/loan_index.xml',
        'views/loan_tracking_views.xml',
        'views/loan_tracking_manus.xml',
        'wizard/loan_wizard_views.xml',
        'report/loan_report.xml',
        'report/loan_deatail.xml',
        'report/loan_doc.xml',
        'data/loan_data.xml',
        'data/mail_template.xml',

    ],


}
