# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    journal_post_group_id = fields.Many2one('res.groups',
                                            string='Journal Post Group',
                                            related='company_id.journal_post_group_id',
                                            readonly=False)

    payment_post_group_id = fields.Many2one('res.groups',
                                            string='Payment Post Group',
                                            related='company_id.payment_post_group_id',
                                            readonly=False)

    asset_post_group_id = fields.Many2one('res.groups',
                                          string='Asset Validate Group',
                                          related='company_id.asset_post_group_id',
                                          readonly=False)
