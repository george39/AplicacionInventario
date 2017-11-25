# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date, time, timedelta
import calendar
from producto.models import Producto

formato = "%d-%m-%y %H:%M %S"
hoy = datetime.today()
cadena2 = hoy.strftime(formato)

# Create your models here.
class Registro(models.Model):
	id_registro = models.CharField(max_length=50)
	id_producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
	nombre_registro = models.CharField(max_length=50)
	cantidad_registro = models.IntegerField()
	fecha_registro = models.DateTimeField(cadena2)


	#para devolver lo que se ve en las llaves foraneas
	def __unicode__(self):
		return '{} - {}'.format(self.id_registro, self.id_producto)
	
