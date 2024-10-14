from odoo import models, fields, api, _

class InheritMyModule(models.Model):
    _inherit = 'new_model.new_model'

    customer_phone_no = fields.Char(
        string='Customer Phone no',
        required=False)
    
    customer_country = fields.Char(
        string='Customer_country',
        required=False)

    expiration_date_2 = fields.Date(
        string='Expiration_date_2', 
        required=False)
    
    quotation_date_2 = fields.Date(
        string='Quotation_date_2', 
        required=False)

    class SaleOrder(models.Model):
        _inherit = 'sale.order'

        taxes_2 = fields.Many2many(
            comodel_name='res.users',
            string='Taxes 2'
        )