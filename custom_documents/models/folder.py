# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Document(models.Model):
    _description = 'Document folder'
    _inherit = 'documents.folder'
    admin_group_ids = fields.Many2many('res.groups',
        string="Groupe d'écriture")

