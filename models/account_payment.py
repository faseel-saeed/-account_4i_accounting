# -*- coding: utf-8 -*-

from collections import defaultdict
import logging
import pprint

from odoo import api, fields, models, _, Command
from odoo.exceptions import UserError, ValidationError, AccessError, RedirectWarning


_logger = logging.getLogger(__name__)


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def customize_user_has_group(self, group_id):
        user = self.env.user
        if group_id in user.groups_id:
            return True
        return False

    def action_post(self):
        payment_post_group_id = self.env.company.payment_post_group_id
        if not payment_post_group_id:
            raise AccessError(_("There are no groups who can post payments. Contact the administrator"))

        user_has_access = self.customize_user_has_group(payment_post_group_id)
        if not user_has_access:
            raise AccessError(_("You don't have the access rights to post a payment."))

        return super(AccountPayment, self).action_post()
