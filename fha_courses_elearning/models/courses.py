from odoo import fields, models, api


class courses_elearning(models.Model):
    _name = 'courses_elearning.courses_elearning'
    _description = 'Visualizador de cursos disponibles para E-Learning'


    #Relación con los cursos disponibles
    course_id = fields.Many2one('slide.channel',string="Curso")
    course_id_user_id = fields.Many2one(related='course_id.user_id', string="Responsable", store=True)
    course_id_total_slides = fields.Integer(related='course_id.total_slides', string="Lecciones")
    course_id_enroll = fields.Selection(related='course_id.enroll', string="Inscritos")
    course_id_completion = fields.Integer(related='course_id.completion', string="Completado")


    

    
    

