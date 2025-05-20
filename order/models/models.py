from odoo import models, fields

class Order(models.Model):
    _name = "custom.order"
    _description = "Order Data"

    name = fields.Char(string="Item Name", required=True)
    orderedby = fields.Text(string="Ordered by", required=True)
    status = fields.Selection([
        ('waiting', 'Waiting'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], string="Status", default="waiting")
    price = fields.Integer(string="Price", default=0)
    date_order = fields.Datetime(string="Order Date", default=fields.Datetime.now)