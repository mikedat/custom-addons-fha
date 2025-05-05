# -*- coding: utf-8 -*-
# from odoo import http


# class FhaFollowersPurchasePermission(http.Controller):
#     @http.route('/fha_followers_purchase_permission/fha_followers_purchase_permission', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fha_followers_purchase_permission/fha_followers_purchase_permission/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fha_followers_purchase_permission.listing', {
#             'root': '/fha_followers_purchase_permission/fha_followers_purchase_permission',
#             'objects': http.request.env['fha_followers_purchase_permission.fha_followers_purchase_permission'].search([]),
#         })

#     @http.route('/fha_followers_purchase_permission/fha_followers_purchase_permission/objects/<model("fha_followers_purchase_permission.fha_followers_purchase_permission"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fha_followers_purchase_permission.object', {
#             'object': obj
#         })
