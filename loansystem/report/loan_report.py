from odoo import models, fields, tools

class LoanReport(models.Model):
    _name = 'loan.report'
    _description = 'Loan Report'
    _auto = False 
    _rec_name = 'id'

    id = fields.Integer()
    state = fields.Selection([
            ('new','New'),
            ('apply','Apply'),
            ('cancel','Cancel'),
            ('draft','Draft'),
            ('approved', 'Approved'),
            ('done','Done')
        ],default='new')
    applicant_apply_id = fields.Many2one('applicant.apply')
    loan_type_id = fields.Many2one('loan.type')


  
