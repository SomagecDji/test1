# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
class DocumentFolder(models.Model):
    _description = 'Document folder'
    _inherit = 'documents.folder'
    admin_group_ids = fields.Many2many('res.groups',  'documents_folder_admin_groups',string="Groupe d'écriture")
    def custom_groups(self):
        folders=self.env['documents.folder'].search([])
        for folder in folders:
            if folder.parent_folder_id:
                parent_folder_id=folder.parent_folder_id.id
                raise UserError(_(folder.group_ids))
                parent_folder=self.env['documents.folder'].search([('id','=',parent_folder_id)])
                if folder.read_group_ids:
                    raise UserError(_(folder.read_group_ids))
                    parent_folder.write({'read_group_ids':[(4, [group.id for group in folder.read_group_ids])]})
                if folder.group_ids:
                    parent_folder.write({'read_group_ids':[(4, [group.id for group in folder.group_ids])]})
                    raise UserError(_(folder.group_ids))
        return()
            

