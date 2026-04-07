# -*- coding: utf-8 -*-
from odoo import fields, models, Command


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    def create_project(self):
        for record in self:
            sale_order_line = record.order_line.search([('id', '=', record.mapped('order_line'))])
            unique_milestones = set(record.mapped('order_line.milestone'))
            project = self.env['project.project'].create({
                'name': record.name
            })

            for milestone in unique_milestones:
                self.env['project.task'].create({
                    'partner_id': record.partner_id.id,
                    'project_id': project.id,
                    'name': milestone,
                })

            task = project.task_ids
            for task in task:
                for order in sale_order_line:
                    if int(task.name) == order.milestone:
                        self.env['project.task'].create({
                            'parent_id': task.id,
                            'name': order.product_template_id.name,
                        })
