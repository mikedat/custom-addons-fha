# -*- coding: utf-8 -*-
# from odoo import http


# class HrMaintenanceDashboard(http.Controller):
#     @http.route('/hr_maintenance_dashboard/hr_maintenance_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_maintenance_dashboard/hr_maintenance_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_maintenance_dashboard.listing', {
#             'root': '/hr_maintenance_dashboard/hr_maintenance_dashboard',
#             'objects': http.request.env['hr_maintenance_dashboard.hr_maintenance_dashboard'].search([]),
#         })

#     @http.route('/hr_maintenance_dashboard/hr_maintenance_dashboard/objects/<model("hr_maintenance_dashboard.hr_maintenance_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_maintenance_dashboard.object', {
#             'object': obj
#         })
