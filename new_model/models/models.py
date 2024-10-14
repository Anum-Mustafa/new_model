from odoo import models, fields, api, _

class NewModel(models.Model):
    _name = 'new_model.new_model'
    _description = 'New Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    # Total Discount Amount field
    total_discount_amount = fields.Float(
        string='Total Discount Amount',
        compute='_compute_total_discount_amount',
        store=True
    )


    @api.depends('orderline_ids.discount_amount')
    def _compute_total_discount_amount(self):
        for record in self:
            record.total_discount_amount = sum(line.discount_amount for line in record.orderline_ids)

    rel_res_company = fields.Many2one(
        comodel_name='res.company',
        string='Rel_res_company',
        required=False)

    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        readonly=True,
        string="Currency")

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company
    )

    customer = fields.Char(
        string='Customer',
        required=False)

    expiration_date = fields.Date(
        string='Expiration',
        required=False)

    payment_term = fields.Selection(
        string='Payment Terms',
        selection=[('1 week', '1 week'), ('20 days', '20 days')],
        required=False)

    qoutation_date = fields.Date(
        string='Quotation Date',
        required=False)

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=False)

    payment_term_id = fields.Many2one(
        comodel_name='account.payment.term',
        string='Payment Term',
        required=False)

    status = fields.Selection(
        [('draft', 'Quotation'),
         ('confirmed', 'Quotation Sent'),
         ('done', 'Sales Order')],
        string='Status',
        default='draft',
        required=True
    )

    sales_person = fields.Many2one(
        comodel_name='res.users',
        string='Sales_person',
        required=False)

    sales_team = fields.Many2one(
        comodel_name='crm.team',
        string='Sales_team',
        required=False)

    online_signature = fields.Boolean(
        string='Online_signature',
        required=False)

    online_payment = fields.Boolean(
        string='Online_payment',
        required=False)

    customer_Reference = fields.Char(
        string='Customer_Reference',
        required=False)

    fiscal_Position = fields.Many2one(
        comodel_name='account.fiscal.position',
        string='Fiscal_Position',
        required=False)

    invoicing_journal = fields.Many2one(
        comodel_name='account.journal',
        string='Invoicing_journal',
        required=False)

    delivery_date = fields.Date(
        string='Delivery_date',
        required=False)

    source_document = fields.Char(
        string='Source_document',
        required=False)

    opportunity = fields.Many2one(
        comodel_name='crm.lead',
        string='Opportunity',
        required=False)

    campaign = fields.Many2one(
        comodel_name='utm.campaign',
        string='Campaign',
        required=False)

    medium = fields.Many2one(
        comodel_name='utm.medium',
        string='Medium',
        required=False)

    source = fields.Many2one(
        comodel_name='utm.source',
        string='Source',
        required=False)

    signed_by = fields.Char(
        string='Signed_by',
        required=False)

    signed_On = fields.Datetime(
        string='Signed_On',
        required=False)

    new_field = fields.Binary(string="Signature", widget="image")

    reference_no = fields.Char(
        string='Order Reference', required=True,
        readonly=True, default=lambda self: _('New'))

    orderline_ids = fields.One2many(
        comodel_name='new_model.order.line',
        inverse_name='order_id',
        string='Orderline_ids',
        required=False)

    optional_product_ids = fields.One2many(
        comodel_name='new_model.optional.product.line',
        inverse_name='new_model_id',
        string='Optional Products',
        required=False)

    untaxed_amount = fields.Float(
        string='Untaxed Amount',
        compute='_compute_total_amounts',
        currency_field='currency_id',
        store=True)

    tax_amount = fields.Float(
        string='Tax Amount',
        compute='_compute_total_amounts',
        currency_field='currency_id',
        store=True)

    total_amount = fields.Float(
        string='Total Amount',
        compute='_compute_total_amounts',
        currency_field='currency_id',
        store=True)

    @api.model
    def create(self, vals):
        if vals.get('reference_no', _('New')) == _('New'):
            vals['reference_no'] = self.env['ir.sequence'].next_by_code(
                'new_model.new_model') or _('New')
        res = super(NewModel, self).create(vals)
        return res

    @api.depends('orderline_ids.computed_field', 'orderline_ids.tax_amount')
    def _compute_total_amounts(self):
        for record in self:
            record.untaxed_amount = sum(line.computed_field for line in record.orderline_ids)
            record.tax_amount = sum(line.tax_amount for line in record.orderline_ids)
            record.total_amount = record.untaxed_amount + record.tax_amount

    def action_test(self):
        print("Button Clicked !!!!!!!")

class OrderLine(models.Model):
    _name = 'new_model.order.line'
    _description = 'Order Line'

    order_id = fields.Many2one('new_model.new_model', string='Order')
    customer_name = fields.Char(string='Customer Name')
    phone_number = fields.Char(string='Phone Number')
    country = fields.Char(string='Country')

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=False)

    unit_price = fields.Float(
        string='Unit Price',
        related='product_id.list_price',
        readonly=True)

    quantity = fields.Float(
        string='Quantity',
        default=1.00,
        required=True)

    description = fields.Char(
        string="Description",
        related='product_id.name',
        readonly=True)

    taxes = fields.Many2many(
        comodel_name='account.tax',
        string='Taxes')

    discount = fields.Float(
        string='Discount',
        required=False)

    discount_amount = fields.Float(
        string='Discount_amount',
        compute='_compute_discount_amount',
        store=True)

    untaxed_amount = fields.Float(
        string='Untaxed Amount',
        compute='_compute_total_amounts',
        store=True)

    tax_amount = fields.Float(
        string='Tax Amount',
        compute='_compute_tax_amount',
        store=True)

    total_amount = fields.Float(
        string='Total Amount',
        compute='_compute_total_amounts',
        store=True)

    computed_field = fields.Float(
        string='Sub Total',
        compute='_compute_computed_field',
        store=True)

    quantity_with_unit = fields.Char(
        string='Quantity',
        compute='_compute_quantity_with_unit',
        store=True
    )

    @api.depends('quantity', 'product_id.uom_id')
    def _compute_quantity_with_unit(self):
        for line in self:
            if line.product_id.uom_id:
                line.quantity_with_unit = f"{line.quantity} {line.product_id.uom_id.name}"
            else:
                line.quantity_with_unit = str(line.quantity)

    @api.depends('quantity', 'unit_price')
    def _compute_computed_field(self):
        for record in self:
            record.computed_field = record.quantity * record.unit_price

    @api.depends('taxes', 'computed_field')
    def _compute_tax_amount(self):
        for record in self:
            total_tax = 0.0
            for tax in record.taxes:
                tax_amount = (record.computed_field * tax.amount) / 100.0
                total_tax += tax_amount
            record.tax_amount = total_tax

    @api.depends('computed_field', 'tax_amount')
    def _compute_total_amounts(self):
        for record in self:
            record.untaxed_amount = record.computed_field
            record.total_amount = record.computed_field + record.tax_amount

    @api.depends('unit_price', 'discount', 'quantity')
    def _compute_discount_amount(self):
        for line in self:
            discount_percentage = line.discount / 100
            line.discount_amount = line.unit_price * line.quantity * discount_percentage

    rel_res_company = fields.Many2one(
        comodel_name='res.company',
        string='Rel_res_company',
        required=False)

    currency_id = fields.Many2one(
        'res.currency',
        related='order_id.company_id.currency_id',
        readonly=True,
        string="Currency")

class OptionalProductLine(models.Model):
    _name = 'new_model.optional.product.line'
    _description = 'Optional Product Line'

    new_model_id = fields.Many2one('new_model.new_model', string='New Model')

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=False)

    unit_price = fields.Float(
        string='Unit Price',
        related='product_id.list_price',
        required=False)

    quantity = fields.Float(
        string='Quantity',
        required=False,
        default=1.00)

    description = fields.Char(
        string="Description",
        related='product_id.name',
        required=False)