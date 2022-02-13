from odoo import models,fields,api


class DocumentsUpload(models.Model):
    _name = 'documents.upload'
    _description = 'Documents Upload'

    adhar_card = fields.Binary(string="Adhar Card")
    doc_name = fields.Char()
    pan_card = fields.Binary(string="Pan Card")
    p_name = fields.Char()
    votersid_card = fields.Binary(string="Voter's Id Card")
    v_name = fields.Char()
    Driving_license = fields.Binary(string="Driving License")
    d_name = fields.Char()
    applicant_apply_id = fields.Many2one('applicant.apply')
