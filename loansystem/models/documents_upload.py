from odoo import models,fields,api


class DocumentsUpload(models.Model):
    _name = 'documents.upload'
    _description = 'Documents Upload'

    adhar_card = fields.Image(string="Adhar Card")
    pan_card = fields.Image(string="Pan Card")
    votersid_card = fields.Image(string="Voter's Id Card")
    Driving_license = fields.Image(string="Driving License")
    applicant_apply_id = fields.Many2one('applicant.apply')
