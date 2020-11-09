# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    # @api.multi
    # def create_forecast(self):
    #     view_id = self.env.ref('project_forecast.project_forecast_view_form').id
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'project.forecast',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'view_id': view_id,
    #         'target': 'current',
    #         'context': {
    #             'default_project_id': self.id,
    #             'default_user_id': self.user_id.id,
    #         }
    #     }


class Task(models.Model):
    _inherit = 'project.task'

   
    @api.multi
    def create_forecast(self):
        view_id = self.env.ref('project_forecast.project_forecast_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.forecast',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_id,
            'target': 'current',
            'context': {
                'default_project_id': self.project_id.id,
                'default_task_id': self.id,
                'default_user_id': self.user_id.id,
                'default_resource_hours': self.planned_hours,
                'default_start_date': self.date_start,
                'default_end_date': self.date_start + + timedelta(days=self.planned_hours/8)
        }
