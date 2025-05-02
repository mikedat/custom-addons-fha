# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Description_purchase(models.Model):
    _inherit = 'purchase.order'

    explication = fields.Text(
        string="Descripción adicional",
        help="Notas o comentarios sobre la orden de compra",
    )
