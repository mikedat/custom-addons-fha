from datetime import date, datetime, timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
""" Modelo para el dashboard de mantenimiento """
class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'
    
    # Campos computados para el dashboard
    dashboard_pending_count = fields.Integer(compute='_compute_dashboard_counts',string="Tareas Pendientes (Dashboard)")
    dashboard_completed_count = fields.Integer(compute='_compute_dashboard_counts',string="Tareas Completadas (Dashboard)")
    pending_day = fields.Boolean(string="Tarea pendiente a un dia", compute='_compute_pending_flags', store=True)
    pending_week = fields.Boolean(string="Tarea pendiente a una semana", compute='_compute_pending_flags', store=True)
    pending_month = fields.Boolean(string="Tarea pendiente a un mes", compute='_compute_pending_flags', store=True)
    pending_halfyear = fields.Boolean(string="Tarea pendiente a 6 meses", compute='_compute_pending_flags', store=True)
    pending_year = fields.Boolean(string="Tarea pendiente a un año", compute='_compute_pending_flags', store=True)
    expired_task = fields.Many2many('maintenance.request',string="Tareas Caducadas",compute='_compute_expired_tasks')
    executed_expired_task = fields.Many2many('maintenance.request',string="Tareas ejecutadas fuera de plazo",compute='_compute_executed_expired_tasks')
    executed_task = fields.Many2many('maintenance.request',string="Tareas Ejecutadas",compute='_compute_executed_tasks')
    pending_task = fields.Many2many('maintenance.request',string="Tareas Pendientes",compute='_compute_pending_tasks')
    pending_task_data = fields.Json(string="Datos de las tareas pendientes", compute="_compute_pending_task_data")
    expired_task_data = fields.Json(string="Datos de las tareas expiradas", compute="_compute_expired_task_data")
    executed_task_data = fields.Json(string="Datos de las tareas ejecutadas", compute="_compute_executed_task_data")
    executed_expired_task_data = fields.Json(string="Datos de las tareas ejecutadas fuera de plazo", compute="_compute_executed_expired_task_data")

    #Función para poder almacenar en formato json las tareas ejecutadas fuera de plazo
    def _compute_executed_expired_task_data(self):
        for record in self:
            executed_expired_tasks_data = []
            for task in record.executed_expired_task:
                    executed_expired_tasks_data.append({
                         'name': task.name,
                         'schedule_date' : fields.Datetime.to_string(task.schedule_date),
                        'user_id': task.user_id.display_name
                    })
            record.executed_expired_task_data = executed_expired_tasks_data

    #Función para poder almacenar en formato json las tareas ejecutadas dentro del plazo
    def _compute_executed_task_data(self):
        for record in self:
            executed_tasks_data = []
            for task in record.executed_task:
                executed_tasks_data.append({
                    'name': task.name,
                    'schedule_date' : fields.Datetime.to_string(task.schedule_date),
                    'user_id': task.user_id.display_name 
                })
            record.executed_task_data = executed_tasks_data
    
    #Función para poder almacenar en formato json las tareas caducadas
    def _compute_expired_task_data(self):
        for record in self:
            expired_tasks_data = []
            for task in record.expired_task:
                expired_tasks_data.append({
                    'name': task.name,
                    'schedule_date' : fields.Datetime.to_string(task.schedule_date),
                    'user_id': task.user_id.display_name 
                })
            record.expired_task_data = expired_tasks_data

    #Función para poder almacenar en formato json las tareas pendientes de ejecutar
    def _compute_pending_task_data(self):
        for record in self:
            pending_tasks_data = []
            for task in record.pending_task:
                pending_tasks_data.append({
                    'name': task.name,
                    'schedule_date':  fields.Datetime.to_string(task.schedule_date),
                    'user_id': task.user_id.display_name    
                })
            record.pending_task_data = pending_tasks_data

    #Función para vincular al botón de "Más Tareas" una acción de menú con sus filtros su vista predefinida para tareas expiradas.
    def open_expired_task_view(self):
        return {
            'name':('Tareas expiradas'),
            'view_mode': 'kanban,tree,form',
            'res_model': 'maintenance.request',
            'type': 'ir.actions.act_window',
            'target': 'main',
            'domain': [('schedule_date', '<', fields.Datetime.today()), ('stage_id.done', '=', False)],
            'views': [
            (self.env.ref('hr_maintenance_dashboard.dashboard_expired_task_view_kanban').id, 'kanban'),
            (self.env.ref('hr_maintenance_dashboard.dashboard_expired_task_view_tree').id, 'tree'),
            (False, 'form')
        ]}
    
    #Función para vincular al botón de "Más Tareas" una acción de menú con sus filtros su vista predefinida para tareas pendientes.
    def open_pending_task_view(self):
        return {
            'name':('Tareas pendientes'),
            'view_mode': 'kanban,tree,form',
            'res_model': 'maintenance.request',
            'type': 'ir.actions.act_window',
            'target': 'main',
            'search_view_id': self.env.ref('hr_maintenance_dashboard.dashboard_filters_view_search').id,
            'context': {
            'search_default_filter_pending_day': True,
            },
            'domain':[('stage_id.done', '=', False), ('schedule_date', '>=', fields.Datetime.today())],
            'views': [
            (self.env.ref('hr_maintenance_dashboard.dashboard_pending_task_view_kanban').id, 'kanban'),
            (self.env.ref('hr_maintenance_dashboard.dashboard_pending_task_view_tree').id, 'tree'),
            (False, 'form')]}

    #Obtenemos los IDs de las tareas expiradas, con estos IDs es con lo que luego podemos formar los Json de arriba 
    def _compute_expired_tasks(self):
        is_admin = self.env.user._is_admin()
        if is_admin:
            domain = [
                ('schedule_date', '<', fields.Datetime.today()),
                ('stage_id.done', '=', False)
            ]
        else:
            user_teams = self.env['maintenance.team'].search([('member_ids', 'in', self.env.user.id)])
            user_team_ids = user_teams.ids
            domain = [
                ('schedule_date', '<', fields.Datetime.today()),
                ('stage_id.done', '=', False),
                ('maintenance_team_id.id', 'in', user_team_ids)
            ]

        tasks = self.env['maintenance.request'].search(domain)

        for record in self:
            record.expired_task = tasks

    #Obtenemos los IDs de las tareas pendientes, con estos IDs es con lo que luego podemos formar los Json de arriba
    def _compute_pending_tasks(self):
        is_admin = self.env.user._is_admin()
        if is_admin:
            domain = [
                ('schedule_date', '>=', fields.Datetime.today()),
                ('stage_id.done', '=', False)
            ]
        else:
            user_teams = self.env['maintenance.team'].search([('member_ids', 'in', self.env.user.id)])
            user_team_ids = user_teams.ids
            domain = [
                ('schedule_date', '>=', fields.Datetime.today()),
                ('stage_id.done', '=', False),
                ('maintenance_team_id.id', 'in', user_team_ids)
            ]

        tasks = self.env['maintenance.request'].search(domain)

        for record in self:
            record.pending_task = tasks

    #Obtenemos los IDs de las tareas ejecutadas pero fuera de plazo, con estos IDs es con lo que luego podemos formar los Json de arriba
    def _compute_executed_expired_tasks(self):
        is_admin = self.env.user._is_admin()
        if is_admin:
            domain = [
                ('schedule_date', '<', fields.Datetime.today()),
                ('stage_id.done', '=', True)
            ]
        else:
            user_teams = self.env['maintenance.team'].search([('member_ids', 'in', self.env.user.id)])
            user_team_ids = user_teams.ids
            domain = [
                ('schedule_date', '<', fields.Datetime.today()),
                ('stage_id.done', '=', True),
                ('maintenance_team_id.id', 'in', user_team_ids)
            ]

        tasks = self.env['maintenance.request'].search(domain)

        for record in self:
            record.executed_expired_task = tasks

    #Obtenemos los IDs de las tareas ejecutadas, con estos IDs es con lo que luego podemos formar los Json de arriba
    def _compute_executed_tasks(self):
        is_admin = self.env.user._is_admin()
        if is_admin:
            domain = [
                ('schedule_date', '>=', fields.Datetime.today()),
                ('stage_id.done', '=', True)
            ]
        else:
            user_teams = self.env['maintenance.team'].search([('member_ids', 'in', self.env.user.id)])
            user_team_ids = user_teams.ids
            domain = [
                ('schedule_date', '>=', fields.Datetime.today()),
                ('stage_id.done', '=', True),
                ('maintenance_team_id.id', 'in', user_team_ids)
            ]

        tasks = self.env['maintenance.request'].search(domain)

        for record in self:
            record.executed_task = tasks

    #Función para obtener el número de las tareas tanto de las pendientes como de las ejecutadas.
    @api.depends('stage_id.done')
    def _compute_dashboard_counts(self):
        # Obtener el número de las tareas
        is_admin = self.env.user._is_admin()
        if is_admin:
            pending = self.env['maintenance.request'].search_count([('stage_id.done', '=', False)])
            completed = self.env['maintenance.request'].search_count([('stage_id.done', '=', True)])
        else:
            user_teams = self.env['maintenance.team'].search([('member_ids', 'in', self.env.user.id)])
            user_team_ids = user_teams.ids
            pending = self.env['maintenance.request'].search_count([('stage_id.done', '=', False),('maintenance_team_id.id', 'in', user_team_ids)])
            completed = self.env['maintenance.request'].search_count([('stage_id.done', '=', True),('maintenance_team_id.id', 'in', user_team_ids)])
        
        # Asignar los valores a los registros
        for record in self:
            record.dashboard_pending_count = pending
            record.dashboard_completed_count = completed

    #Calculamos cuanto le falta a la tarea para ser ejectuada
    @api.depends('schedule_date', 'done')
    def _compute_pending_flags(self):
        #Obtenenemos el día actual
        today = fields.Datetime.today()
        for record in self:
            #Ponemos en False todos los campos.
            record.pending_day = False
            record.pending_week = False
            record.pending_month = False
            record.pending_halfyear = False
            record.pending_year = False

            if not record.schedule_date or record.done:
                continue
            
            #Obtenemos la diferencia de días en base a la fecha agendada para la tarea en cuestión
            delta = (record.schedule_date - today ).days

            #dependiendo de la diferencia de días uno de los campos de pondrá en True.
            if delta <= 0:
                record.pending_day = True
            elif delta <= 7:
                record.pending_week = True
            elif delta <= 30:
                record.pending_month = True
            elif delta <= 180:
                record.pending_halfyear = True
            elif delta <= 365:
                record.pending_year = True

