# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mymodule(models.Model):
<<<<<<< HEAD

    _name = 'academy.course'

    name = fields.Char(string="Title", required=True)
=======
    _name = 'academy.course'

    title = fields.Char(string="Title", required=True)
>>>>>>> 36e6633367190ef4ea603210c970ef5c87f4dd95
    description = fields.Text()