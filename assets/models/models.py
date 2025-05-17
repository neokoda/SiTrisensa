from odoo import models, fields

class Asset(models.Model):
    _name = "custom.asset"
    _description = "Asset Data"

    name = fields.Char(string="Asset Name", required=True)
    description = fields.Text(string="Description")
    stock = fields.Integer(string="Stock", default=0)
    price = fields.Integer(string="Price", default=0)
