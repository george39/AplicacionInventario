# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from producto.models import Producto
from distribuidor.models import Distribuidor

# Create your models here.
class Compra(models.Model):
	codigo_compra = models.CharField(max_length=50, primary_key=True,)
	id_producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
	nit_proveedor = models.ForeignKey(Distribuidor, null=True, blank=True, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	valor_compra = models.IntegerField()
	#fecha = models.DateTimeField()#(auto_now_add=True, auto_now=False)


	def __unicode__(self):
		return '{} - {}'.format(self.codigo_compra, self.id_producto)
