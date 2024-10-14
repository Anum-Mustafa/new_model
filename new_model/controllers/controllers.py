# -*- coding: utf-8 -*-
# from odoo import http


# class NewModel(http.Controller):
#     @http.route('/new_model/new_model', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_model/new_model/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_model.listing', {
#             'root': '/new_model/new_model',
#             'objects': http.request.env['new_model.new_model'].search([]),
#         })

#     @http.route('/new_model/new_model/objects/<model("new_model.new_model"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_model.object', {
#             'object': obj
#         })

