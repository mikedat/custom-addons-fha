# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hr_timesheet_chief_department(models.Model):
#     _name = 'hr_timesheet_chief_department.hr_timesheet_chief_department'
#     _description = 'hr_timesheet_chief_department.hr_timesheet_chief_department'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
