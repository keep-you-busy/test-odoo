from odoo import fields, models, api
import random
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_test = fields.Char(string='Test', readonly=True, states={'draft': [('readonly', False)]})

    @api.onchange('order_line', 'date_order')
    def _onchange_test(self):
        if self.state == 'draft':
            total = sum(line.price_total for line in self.order_line)
            date = self.date_order.strftime('%m/%d/%Y %H:%M:%S')
            self.test = '{} - {}'.format(total, date)

    @api.model
    def create(self, vals):
        if 'x_test' not in vals:
            vals['x_test'] = str(random.randint(0, 1000))
        return super().create(vals)

    def write(self, vals):
        if 'x_test' in vals and len(vals['x_test']) > 50:
            raise ValidationError('Длина текста должна быть меньше 50 символов!')
        return super().write(vals)
