from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal

class Mycontroller(portal.CustomerPortal):

    @http.route('/loan', type="http", auth="public", website=True)
    def loan_show(self, **kw):
        loan_res = request.env['loan.type'].sudo().search([])
        print(">>>>>>>>>>>.", loan_res)
        
        return http.request.render('loansystem.loans_static', {'applicant_name': 'john','loan_res':loan_res})

    @http.route('/create/webloanapply', type="http", auth="public", website=True)
    def create_weblogin(self, **kw):
        print("Data Received.....", kw)
        ln=request.env['applicant.apply'].sudo().create(kw)
        print(ln)
        return request.render("loansystem.loan_details", {'ln':ln})
        
    # @http.route('/applicant_apply', website=True)
    # def student_form(self, **kw):
    #     ln=request.render("loansystem.applicant_apply")
    #     print(ln)
    #     return request.render("loansystem.loan_details", {'ln':ln})
