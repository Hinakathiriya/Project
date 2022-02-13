from odoo import models,fields,api


class LoanType(models.Model):
    _name = 'loan.type'
    _description = 'Loan Type'

    loan_name = fields.Char()
    description = fields.Text()
    interest_rate = fields.Integer()