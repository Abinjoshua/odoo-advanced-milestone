# -*- coding: utf-8 -*-
from odoo import fields, models, Command


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    def create_project(self):
        product = self.mapped('order_line.product_template_id')
        self.env['project.task'].create({
            'project_id': 5,
            'partner_id': self.partner_id.id,
            'name': self.name,
            # 'invoice_date': fields.Date.today(),
            # 'credit_date': cred_date,
            'child_ids': [
                Command.create({
                    'name': product[0].name,
                #     'quantity': 1,
                #     'product_id': sub.product_id.id,
                #     'price_unit': sub.recurring_amount
                })
            ],

        })