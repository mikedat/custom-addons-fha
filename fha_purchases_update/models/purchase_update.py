# Copyright 2022 Xtendoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    #Campo para seguidores de compras
    is_follower=fields.Boolean(string="Eres seguidor", compute='_compute_is_follower',  search='_search_is_follower')

    #Campos para todos los usuarios
    calification = fields.Selection(
        [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        "Calificación",
        default="0",
        tracking=True,
    )
    explication = fields.Text(
        string="Descripción adicional",
        help="Notas o comentarios sobre la orden de compra",
    )

    delivery_delay = fields.Boolean(
        string="Retraso en la entrega",
        help="Marcar si ha habido un retraso en la entrega del pedido",
        default=False)
    
    bad_material = fields.Boolean(
        string="Material defectuoso",
        help="Marcar si el material recibido es defectuoso",
        default=False)
    
    incomplete_material = fields.Boolean(
        string="Material incompleto",
        help="Marcar si el material recibido es incompleto",
        default=False)
    
    # Campos para el grupo de Administradores de Compras
    #Incidencias adminitrativas
    invoice_wrong = fields.Boolean(
        string="Factura errónea",
        help="Marcar si la factura es errónea",
        default=False)
    
    no_receipt_invoice = fields.Boolean(
        string="No recepción de factura",
        help="Marcar si la factura no ha sido recibida",
        default=False)

    #Incidencias Internas
    bad_request = fields.Boolean(
        string="Solicitud mal hecha",
        help="Marcar si la solicitud de pedido es errónea",
        default=False)

    bad_approved_request = fields.Boolean(
        string="Solicitud mal aprobada",
        help="Marcar si la solicitud del pedido ha sido aprobada erróneamente",
        default=False)

    no_send_invoice_admin_dpto = fields.Boolean(
        string="No se ha enviado la factura al departamento de administración",
        help="Marcar si la factura no ha sido enviada al departamento de administración",
        default=False)
    
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

BASE_EXCEPTION_FIELDS = ["message_follower_ids", "access_token", "calification"]

class TierValidation(models.AbstractModel):
    _inherit = "tier.validation"
    _description = "Tier Validation (abstract)"

    @api.model
    def _get_validation_exceptions(self, extra_domain=None, add_base_exceptions=True):
        """Return Tier Validation Exception field names that matchs custom domain."""
        exception_fields = (
            self.env["tier.validation.exception"]
            .sudo()
            .search(
                [
                    ("model_name", "=", self._name),
                    ("company_id", "in", [False] + self.env.company.ids),
                    "|",
                    ("group_ids", "in", self.env.user.groups_id.ids),
                    ("group_ids", "=", False),
                    *(extra_domain or []),
                ]
            )
            .mapped("field_ids.name")
        )
        if add_base_exceptions:
            exception_fields += BASE_EXCEPTION_FIELDS
        return list(set(exception_fields))
