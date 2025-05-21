# Copyright 2017 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _ 
from odoo.exceptions import UserError, ValidationError


class hr_leave(models.Model):
    _name = "hr.leave"
    _inherit = ["hr.leave", "tier.validation"]
    _state_from = ["draft", "confirm", "validate1"]
    _state_to = ["validate"]
    _tier_validation_manual_config = False
    
    # Sobrescribir el método action_approve
    def fha_action_approve(self):
        for record in self:
            try:
                record.sudo()._validate_tier()
            except ValidationError as e:
                raise e
            except UserError as e:
                raise e
            except Exception as e:
                self.env.cr.rollback()
                raise UserError(_("An unexpected error occurred during approval: %s") % e)

        return True 
    
    def fha_action_validate(self):
        for record in self:
            try:
                record.sudo()._validate_tier()
            except ValidationError as e:
                raise e
            except UserError as e:
                raise e
            except Exception as e:
                self.env.cr.rollback()
                raise UserError(_("An unexpected error occurred during validation: %s") % e)

        return True 

    def fha_action_refuse(self):
        for record in self:
            try:
                record.sudo()._refuse_tier()
            except ValidationError as e:
                raise e
            except UserError as e:
                raise e
            except Exception as e:
                self.env.cr.rollback()
                raise UserError(_("An unexpected error occurred during refusal: %s") % e)

        return True

    