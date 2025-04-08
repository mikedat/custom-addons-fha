# -*- coding: utf-8 -*-
# from odoo import http


# class HrPurchasesMod(http.Controller):
#     @http.route('/hr_purchases_mod/hr_purchases_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_purchases_mod/hr_purchases_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_purchases_mod.listing', {
#             'root': '/hr_purchases_mod/hr_purchases_mod',
#             'objects': http.request.env['hr_purchases_mod.hr_purchases_mod'].search([]),
#         })

#     @http.route('/hr_purchases_mod/hr_purchases_mod/objects/<model("hr_purchases_mod.hr_purchases_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_purchases_mod.object', {
#             'object': obj
#         })
