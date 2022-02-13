from calendar import month
from email.policy import default
from hashlib import new
from locale import currency
from odoo import models,fields,api
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta

class ApplicantApply(models.Model):
    _name = 'applicant.apply'
    _description = 'Applicant can aaply'
    # _sql_constraints = [('Positiv Amount', 'check(amount>0)', 'Enter positive value')]


   
    @api.depends('amount', 'rate')
    def _compute_amount(self):
        for record in self:
            record.total= record.amount + record.amount * record.rate/100
        
    # def _inverse_amount(self):
    #     for record in self:
    #         record.amount = record.rate = record.total / 2

    applicant_name = fields.Char(string="Name", default="Unknown", required=True)
    mobile_no = fields.Integer()
    email = fields.Char()
    loan_type_id = fields.Many2one('loan.type',string="Loan Type",required=False)
    apply_date = fields.Date()
    approve_date = fields.Date()
    image = fields.Image()
    currency_id = fields.Many2one('res.currency')
    amount = fields.Monetary(currency_field='currency_id')
    # amount = fields.Float()
    is_interest_payable = fields.Boolean()
    interest_mode = fields.Char(default='Flat',readonly=True)
    duration = fields.Char(default='Monthly',readonly=True)
    rate = fields.Integer(default=10,readonly=True)
    state = fields.Selection([
            ('new','New'),
            ('apply','Apply'),
            ('cancel','Cancel'),
            ('draft','Draft'),
            ('approved', 'Approved'),
            ('done','Done')
        ],default='new')
    document_ids = fields.One2many('documents.upload','applicant_apply_id')
    total = fields.Float(compute=_compute_amount)
    currency_id = fields.Many2one('res.currency', string='Currency', store=True, readonly=False)

    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount > 500000:
                raise ValidationError("Amount cannot be bigger than 500000")


    def action_apply(self):
        for record in self:
            record.state = 'apply'
    
    def action_cancel(self):
        for record in self:
            if record.state == 'apply':
                raise UserError("If Once You have apply than it's not cancel")
            record.state = 'cancel'

    def action_approved(self):
         for record in self:
            if record.state == 'cancel':
                raise UserError("approved loan can not be cancel")
            record.state = 'approved'
    
    def action_draft(self):
        for record in self:
            record.state = 'draft'
        
      
    def action_done(self):
        for record in self:
            record.state = 'done'



