from unicodedata import name
from odoo import fields, models


class LoanWizard(models.TransientModel):
    _name = 'loan.wizard'
    _description = 'Loan Wizard'

    name = fields.Char()
    discription = fields.Text()
    

    def action_make_loan(self):
        activeIds = self.env.context.get('active_ids')
        for i in activeIds:
            self.env['loan.type'].create({'name':self.name})
        return True