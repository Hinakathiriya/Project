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
    _rec_name = 'applicant_name'
    _inherit = ['mail.thread']
    # _sql_constraints = [('Positiv Amount', 'check(amount>0)', 'Enter positive value')]

   
    @api.depends('amount', 'rate')
    def _compute_amount(self):
        for record in self:
            record.total= record.amount + record.amount * record.rate/100
    
    
        
    # employee_id = fields.Many2one('hr.employee', string="User Name",required=True)   
    ref_seq = fields.Char(string="Reference ID", default=lambda self:_('New'))
    applicant_name = fields.Char(string="Name", default="Unknown", required=True)
    mobile_no = fields.Char()
    email = fields.Char()
    partner_id = fields.Many2one('res.partner')
    loan_type_id = fields.Many2one('loan.type',string="Loan Type")
    apply_date = fields.Date()
    approve_date = fields.Date()
    image = fields.Image()
    currency_id = fields.Many2one('res.currency')
    amount = fields.Monetary(currency_field='currency_id')
    is_interest_payable = fields.Boolean()
    interest_mode = fields.Selection([
            ('flat','Flat'),
            ('floating','Floating')
        ])
    duration = fields.Selection([
            ('weekly','Weekly'),
            ('monthly','Monthly'),
            ('Yearly','Yearly')
        ])
    rate = fields.Integer(default=10,readonly=True)
    state = fields.Selection([
            ('new','New'),
            ('apply','Apply'),
            ('cancel','Cancel'),
            ('draft','Draft'),
            ('approved', 'Approved'),
            ('done','Done'),
        ],default='new')
    document_ids = fields.One2many('documents.upload','applicant_apply_id')
    total = fields.Float(compute=_compute_amount)
    currency_id = fields.Many2one('res.currency', string='Currency', store=True, readonly=False)
    loan_installment_ids = fields.One2many('loan.installment','applicant_apply_id')

    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount > 500000:
                raise ValidationError("Amount cannot be bigger than 500000")

    @api.model
    def create(self, vals):
        print("\n Create method is called ", vals)
        if vals.get('ref_seq', 'New') == 'New':
            vals['ref_seq'] = self.env['ir.sequence'].next_by_code('loan.seq')
        r = super(ApplicantApply, self).create(vals)
        return r

    def write(self, vals):
        print("\n Write method is called ", vals)
        return super(ApplicantApply, self).write(vals)

    def action_apply(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("If Once You have apply than it's not cancel")
            record.state = 'apply'
    
    def action_cancel(self):
        for record in self:
            if record.state == 'apply' or 'approved':
                raise UserError("If Once You have cancel than it's not apply")
            record.state = 'cancel'

    def action_approved(self):
         for record in self:
            if record.state == 'cancel':
                raise UserError("once loan is approved than it's not be cancel or apply")
            record.state = 'approved'
    
    def action_draft(self):
        for record in self:
            record.state = 'draft'
        
      
    def action_done(self):
            for record in self:
                if record.state == 'aproved':
                    raise UserError("once loan is done than it's not be approve")
                record.state = 'done'

    def action_send_mail(self):
        print("Sending mail......................")
        template_id = self.env.ref('loansystem.loan_card_email_template').id
        print("templetae id",template_id)
        template = self.env['mail.template'].browse(template_id)
        print("templete.........",template)
        #self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
        template.send_mail(self.id,force_send=True)
        


