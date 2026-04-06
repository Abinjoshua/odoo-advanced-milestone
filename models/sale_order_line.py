# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesOrderLine(models.Model):
    _inherit = "sale.order.line"

    milestone = fields.Integer(string="Milestone Tasks")