# Copyright 2017 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class hr_leave(models.Model):
    _name = "hr.leave"
    _inherit = ["hr.leave", "tier.validation"]
    _state_from = ["draft", "confirm"]
    _state_to = ["validate"]
    _tier_validation_manual_config = False
    