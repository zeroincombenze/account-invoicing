
from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    date_currency = fields.Date(
        string='Currency Date')
