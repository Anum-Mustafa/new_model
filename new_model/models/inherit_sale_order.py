from odoo import models, fields


class NewModelOrderLine(models.Model):
    _inherit = 'new_model.order.line'  # Ensure this matches your actual model name
    _description = 'Order Line'

    
    inherit_tax = fields.Char(
        string='Inherit_tax', 
        required=False)
    
class MyNewModelOptionalProductLine(models.Model):
    _inherit = 'new_model.optional.product.line'
    _description = 'Optional Product Line'
    
    inherit_quantity = fields.Char(
        string='Inherit_quantity', 
        required=False)
