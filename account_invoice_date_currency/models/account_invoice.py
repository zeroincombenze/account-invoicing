
from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    date_currency = fields.Date(
        string='Currency Date')

    # @api.model_cr
    def _register_hook(self):

        @api.multi
        def get_custom_currency_rate_date(self):
            return self.date_currency or self.date_invoice or self.date

        self._patch_method("_get_currency_rate_date",
                           get_custom_currency_rate_date)
        return super()._register_hook()
