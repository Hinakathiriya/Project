from email.policy import default
from importlib.metadata import requires
import string
from odoo import models,fields,api

class LoanInstallment(models.Model):
    _name  = 'loan.installment'

    @api.depends('interest_rate','emi')
    def _compute_emi(self):
        for record in self:
            record.total = record.interest_rate * record.emi+record.emi/100


    applicant_apply_id = fields.Many2one('applicant.apply')
    interest_rate = fields.Float(string="Interest Rate",default=10)
    emi = fields.Float(string = "Installment(EMI)",required=True)
    total = fields.Float(compute=_compute_emi)
