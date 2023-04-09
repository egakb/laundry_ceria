# -*- coding: utf-8 -*-

from odoo import api, fields, models

class LaundryOrder(models.Model):
    _name = "laundry.order"
    _description = "Laundry"

    name = fields.Char(string="Name")
    order_date = fields.Date(string="Date", default=fields.Date.today)
    finish_date = fields.Date(string="Est Finish")
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
    )
    partner_phone = fields.Char(string="Phone")
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsible',
        default=lambda self: self.env.user,
    )
    state = fields.Selection(selection=[
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('ready_pickup','Ready Pickup'),
        ('done','Done'),
        ('cancel','Cancel')
    ],string="State", default='draft', required=True, copy=False)
    laundry_line_ids = fields.One2many(
        comodel_name='laundry.order.line',
        inverse_name='laundry_order_id',
        string='Laundry line',
    )
    note = fields.Text(string="Note")
    total_amount = fields.Float(string="Total")

class LaundryOrderLine(models.Model):
    _name = "laundry.order.line"
    _description = "Laundry Lines"

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product'
    )
    description = fields.Char(string="Desc")
    laundry_order_id = fields.Many2one(
        comodel_name='laundry.order',
        string='Laundry Order',
    )
    unit_price = fields.Float(string="Unit Price")
    quantity = fields.Integer(string="Quantity")
    amount = fields.Float(string="Amount")