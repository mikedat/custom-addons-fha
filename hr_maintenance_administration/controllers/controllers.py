# -*- coding: utf-8 -*-
# from odoo import http


# class HrMaintenanceAdministration(http.Controller):
#     @http.route('/hr_maintenance_administration/hr_maintenance_administration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_maintenance_administration/hr_maintenance_administration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_maintenance_administration.listing', {
#             'root': '/hr_maintenance_administration/hr_maintenance_administration',
#             'objects': http.request.env['hr_maintenance_administration.hr_maintenance_administration'].search([]),
#         })

#     @http.route('/hr_maintenance_administration/hr_maintenance_administration/objects/<model("hr_maintenance_administration.hr_maintenance_administration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_maintenance_administration.object', {
#             'object': obj
#         })
