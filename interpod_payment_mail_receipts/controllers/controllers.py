# -*- coding: utf-8 -*-
from odoo import http

# class InterpodQuality(http.Controller):
#     @http.route('/interpod_quality/interpod_quality/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_quality/interpod_quality/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_quality.listing', {
#             'root': '/interpod_quality/interpod_quality',
#             'objects': http.request.env['interpod_quality.interpod_quality'].search([]),
#         })

#     @http.route('/interpod_quality/interpod_quality/objects/<model("interpod_quality.interpod_quality"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_quality.object', {
#             'object': obj
#         })