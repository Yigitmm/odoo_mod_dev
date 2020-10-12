# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)
    category_id = fields.Many2one('res.partner.category', string="Category")

    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)

    
class PartnerCategory(models.Model):
    _name = 'res.partner.category'
    _description = 'Partner Category'
    
    name = fields.Char('Category')