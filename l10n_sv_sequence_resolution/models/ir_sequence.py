# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import pytz
from dateutil import tz
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    use_mh_control = fields.Boolean(string='Use MH Resolutions Control?')
    remaining_numbers = fields.Integer(string='Remaining Numbers',
                                       default=False)
    remaining_days = fields.Integer(string='Remaining Days', default=False)
    mh_class = fields.Selection(selection=[
        ('1', 'IMPEROSO POR IMPRENTA O TIQUETES'), ('2', 'FORMULARIO UNICO')
    ],
                                string='Class Document')
