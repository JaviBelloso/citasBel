# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class citasbel_cita(models.Model):
	_name = 'citasbel.cita'
	
	autor = fields.Char(string='Autor', required=True, help='Autor de la Cita')
	cita = fields.Text('Cita', required=True, help='Texto de la Cita')
	fecha = fields.Datetime(string='Fecha de visualizacion', required=True, help='Fecha de visualizacion')
        orden = fields.Integer(string='Orden de visualizacion', required=True, help='Orden de visualizacion')