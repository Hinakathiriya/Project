from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal

class Mycontroller(portal.CustomerPortal):

    @http.route('/loan', type="http", auth="public", website=True)
    def loan_show(self, **kw):
        return http.request.render('loansystem.loans_static', {'name': 'john','loan.type':'loan_type_id'})

    @http.route('/create/webloanapply', type="http", auth="public", website=True)
    def create_weblogin(self, **kw):
        print("Data Received.....", kw)
        request.env['applicant.apply'].sudo().create(kw)
        return request.render("loansystem.user_thanks", {})