# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class IrSequenceDateRange(models.Model):
    _inherit = 'ir.sequence.date_range'

    use_mh_control = fields.Boolean(string='Use MH Resolutions Control?',
                                    related='sequence_id.use_mh_control',
                                    store=False)
    prefix = fields.Char(string='Prefix')
    resolution_number = fields.Char(string='Resolution Number')
    number_from = fields.Integer(string='Initial Number', default=False)
    number_to = fields.Integer(string='Final Number', default=False)
    active_resolution = fields.Boolean(string='Active Resolution?')
