# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from registro.models import Registro
from datetime import datetime, date, time, timedelta
import calendar



# Create your models here.
formato = "%d-%m-%y %H:%M %S"
hoy = datetime.today()

cadena2 = hoy.strftime(formato)

class Venta(models.Model):
	codigo_venta = models.CharField(max_length=50, primary_key=True,)
	id_producto = models.ForeignKey(Registro, null=True, blank=True, on_delete=models.CASCADE)
	fecha_venta = models.DateField()
	cantidad = models.IntegerField()
	valor_venta = models.IntegerField()


	def __unicode__ (self):
		return '{} - {}'.format(self.codigo_venta, self.id_producto)