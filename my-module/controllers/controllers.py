# -*- coding: utf-8 -*-
from odoo import http

# class My-module(http.Controller):
#     @http.route('/my-module/my-module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my-module/my-module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my-module.listing', {
#             'root': '/my-module/my-module',
#             'objects': http.request.env['my-module.my-module'].search([]),
#         })

#     @http.route('/my-module/my-module/objects/<model("my-module.my-module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my-module.object', {
#             'object': obj
#         })