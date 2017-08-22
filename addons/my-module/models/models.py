# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mymodule(models.Model):
    _name = 'academy.course'

    title = fields.Char(string="Title", required=True)
    description = fields.Text()