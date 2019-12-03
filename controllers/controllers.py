# -*- coding: utf-8 -*-
from odoo import http

# class VitPrTracking(http.Controller):
#     @http.route('/vit_pr_tracking/vit_pr_tracking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_pr_tracking/vit_pr_tracking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_pr_tracking.listing', {
#             'root': '/vit_pr_tracking/vit_pr_tracking',
#             'objects': http.request.env['vit_pr_tracking.vit_pr_tracking'].search([]),
#         })

#     @http.route('/vit_pr_tracking/vit_pr_tracking/objects/<model("vit_pr_tracking.vit_pr_tracking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_pr_tracking.object', {
#             'object': obj
#         })