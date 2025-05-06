from odoo import api, fields, models

class follower_purchase_model(models.Model):
    _inherit = 'purchase.order'

    #Campo computado para poder filtrar por orden seguida
    is_follower=fields.Boolean(string="Eres seguidor", compute='_compute_is_follower',  search='_search_is_follower')

    #Función computada para poder calcular si eres seguidor o no de una compra
    def _compute_is_follower(self):
        current_partner = self.env.user.partner_id
        for record in self:
            record.is_follower = current_partner in record.message_partner_ids

    # Función de búsqueda para permitir filtrar por este campo
    def _search_is_follower(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            return []
            
        current_partner = self.env.user.partner_id
        if (operator == '=' and value) or (operator == '!=' and not value):
            return [('message_partner_ids', 'in', [current_partner.id])]
        else:
            return [('message_partner_ids', 'not in', [current_partner.id])]