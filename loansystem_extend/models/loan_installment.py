from email.policy import default
from importlib.metadata import requires
import string
from odoo import models,fields,api

class LoanSystemExtend(models.Model):
    _inherit = 'applicant.apply'

    additional_details = fields.Text()

class LoanInstallment(models.Model):
    _name  = 'loan.installment'
    _inherits = {'applicant.apply':'applicant_apply_id'}

    @api.depends('interest_amount','emi')
    def _compute_emi(self):
        for record in self:
            record.total = record.interest_amount * record.emi/100

    applicant_apply_id = fields.Many2one('applicant.apply')
    interest_amount = fields.Float(string="Interest Amount",default=10)
    emi = fields.Float(string = "Installment",required=True)
    total = fields.Float(compute=_compute_emi)
    # applicant_apply_id = fields.Many2one('applicant.apply')
