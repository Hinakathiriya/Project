from email.policy import default
from importlib.metadata import requires
import string

from blinker import receiver_connected
from odoo import models,fields,api

class LoanInstallment(models.Model):
    _name  = 'loan.installment'
    _rec_name = 'applicant_apply_id'

    @api.depends('emi','emi_month','interest_rate')
    def _compute_emi(self):
        for rec in self:
            rec.total = 0.0
            if rec.emi and rec.emi_month and rec.interest_rate:
                amt = rec.emi
                mth = rec.emi_month
                int_r = rec.interest_rate 
                k = 12
                i = int_r/100
                a = i/k if i/k else 0.00
                b = (1 - (1/((1+(i/k))**mth)))
                rec.total = ( ( amt * a ) / b ) or 0.00
            

    applicant_apply_id = fields.Many2one('applicant.apply')
    emi = fields.Float(string = "Amount",required=True)
    interest_rate = fields.Float(string="Interest Rate")
    emi_month = fields.Integer(string="EMI Month")
    total = fields.Float(string="Total Payable Amount", compute=_compute_emi,readonly=1)
