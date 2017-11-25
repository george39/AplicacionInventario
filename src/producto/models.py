# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
	id_producto = models.CharField(max_length=50, primary_key=True)
	nombre_producto = models.CharField(max_length=50)
	precio_producto = models.IntegerField()

	def __unicode__(self):
		return '{}'.format(self.id_producto)

	
