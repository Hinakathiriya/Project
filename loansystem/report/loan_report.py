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


    # def _select(self):
    #     return """
    #         epo.id as id,
    #         epo.state as loan_state,
    #         epo.applicant_apply_id as applicant_apply_id,
    #         ap.loan_type_id as loan_type_id
    #     """
    # def _from(self):
    #     return """
    #     applicant_apply as ap join loan_type as epo on epo.applicant_apply_id = ap.id
    #     """

    # def init(self):
    #     # PRovide what to do with this model -> create 
    #     tools.drop_view_if_exists(self._cr, self._table)
    #     self._cr.execute("""create or replace view %s as (
    #         select %s from %s)
    #         """ % (self._table, self._select(), self._from()))

    # select col1,col2,col3 from Table name