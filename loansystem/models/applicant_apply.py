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


    @api.depends('apply_date', 'approve_date')
    def _get_duration(self):
        for record in self:
            if record.approve_date and record.apply_date:
                diff = record.approve_date - record.apply_date
                record.duration = diff.days
            else:
                record.duration = 1

    def _set_duration(self):
        for record in self:
            record.approve_date = record.apply_date + relativedelta(days=record.duration)



    name = fields.Char(string="Name", default="Unknown", required=True)
    mobile_no = fields.Integer()
    email = fields.Char()
    loan_type_id = fields.Many2one('loan.type',string="Loan Type",required=True)
    apply_date = fields.Date()
    approve_date = fields.Date()
    image = fields.Image()
    currency_id = fields.Many2one('res.currency')
    amount = fields.Float()
    is_interest_payable = fields.Boolean()
    interest_mode = fields.Char(default='Flat',readonly=True)#selection
    duration = fields.Integer(compute=_get_duration, inverse=_set_duration)
    rate = fields.Integer()
    state = fields.Selection([
            ('new','New'),
            ('apply','Apply'),
            ('cancel','Cancel'),
            ('draft','Draft'),
            ('approved', 'Approved'),
            ('done','Done')
        ],default='new')
    document_ids = fields.One2many('documents.upload','applicant_apply_id')
    


    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount > 500000:
                raise ValidationError("Amount cannot be bigger than 500000")

    # @api.onchange('')
    # def _onchange_garden(self):
    #     for record in self:
    #         if record.garden:
    #             record.rate = 10
    #             record.is_interest_payable = 'true'
    #         else:
    #             record.rate = 0
    #             record.is_interest_payable = None

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



