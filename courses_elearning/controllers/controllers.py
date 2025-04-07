# -*- coding: utf-8 -*-
# from odoo import http


# class CoursesElearning(http.Controller):
#     @http.route('/courses_elearning/courses_elearning', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/courses_elearning/courses_elearning/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('courses_elearning.listing', {
#             'root': '/courses_elearning/courses_elearning',
#             'objects': http.request.env['courses_elearning.courses_elearning'].search([]),
#         })

#     @http.route('/courses_elearning/courses_elearning/objects/<model("courses_elearning.courses_elearning"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('courses_elearning.object', {
#             'object': obj
#         })
