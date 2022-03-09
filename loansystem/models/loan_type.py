from odoo import models,fields,api


class LoanType(models.Model):
    _name = 'loan.type'
    _description = 'Loan Type'
    _rec_name = 'loan_name'

    loan_name = fields.Char()
    description = fields.Text()
    interest_rate = fields.Integer()
    applicant_apply_id = fields.One2many('applicant.apply','loan_type_id')