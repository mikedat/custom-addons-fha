# -*- coding: utf-8 -*-
# from odoo import http


# class HrTimesheetChiefDepartment(http.Controller):
#     @http.route('/hr_timesheet_chief_department/hr_timesheet_chief_department', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_timesheet_chief_department/hr_timesheet_chief_department/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_timesheet_chief_department.listing', {
#             'root': '/hr_timesheet_chief_department/hr_timesheet_chief_department',
#             'objects': http.request.env['hr_timesheet_chief_department.hr_timesheet_chief_department'].search([]),
#         })

#     @http.route('/hr_timesheet_chief_department/hr_timesheet_chief_department/objects/<model("hr_timesheet_chief_department.hr_timesheet_chief_department"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_timesheet_chief_department.object', {
#             'object': obj
#         })
