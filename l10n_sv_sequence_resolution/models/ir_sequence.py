# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    use_dgii_control = fields.Boolean(string='Use DGII Resolutions Control?')
    remaining_numbers = fields.Integer(string='Remaining Numbers',
                                       default=False)
    remaining_days = fields.Integer(string='Remaining Days', default=False)
    dgii_class = fields.Selection(selection=[('1',
                                              'PRINTED BY PRINTER OR TICKETS'),
                                             ('2', 'SINGLE FORM')],
                                  string='Class Document')
