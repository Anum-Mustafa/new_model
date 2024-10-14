from odoo import models, fields, api

class Customer(models.Model):
     _name = 'new_model.customer'
     _description = 'new_model.new_model'
     
     customer = fields.Char(
         string='Customer', 
         required=False)
     
     street = fields.Char(
         string='Street', 
         required=False)
     
     country = fields.Char(
         string='Country', 
         required=False)
     
     city = fields.Char(
         string='City', 
         required=False)
     
     tax_id = fields.Char(
         string='Tax_ID', 
         required=False)

     job_position = fields.Char(
         string=' job_position',
         required=False)

     phone = fields.Char(
         string=' Phone',
         required=False)

     mobile = fields.Char(
         string=' Mobile',
         required=False)

     email = fields.Char(
         string=' Email',
         required=False)

     website = fields.Char(
         string=' Website',
         required=False)