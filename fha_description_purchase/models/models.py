# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fha_description_purchase(models.Model):
#     _name = 'fha_description_purchase.fha_description_purchase'
#     _description = 'fha_description_purchase.fha_description_purchase'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
