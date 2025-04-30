# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseDepartments(http.Controller):
#     @http.route('/purchase_departments/purchase_departments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_departments/purchase_departments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_departments.listing', {
#             'root': '/purchase_departments/purchase_departments',
#             'objects': http.request.env['purchase_departments.purchase_departments'].search([]),
#         })

#     @http.route('/purchase_departments/purchase_departments/objects/<model("purchase_departments.purchase_departments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_departments.object', {
#             'object': obj
#         })
