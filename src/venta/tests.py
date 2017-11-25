# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from venta.models import Venta
from datetime import datetime, date, time, timedelta
import calendar

formato = "%d-%m-%y %H:%M %S"
hoy = datetime.today()

cadena2 = hoy.strftime(formato)

# Create your tests here.
class VentaTest(TestCase):
	def setUp(self):
		Venta.objects.create(codigo_venta='3', fecha_venta='2017-10-01', cantidad=4, valor_venta=5)


	def test_codigo_venta(self):  
		codigo = Venta.objects.get(codigo_venta='3')
		self.assertEqual(codigo.codigo_venta, '3')

	def test_cantidad(self):
		cantidad = Venta.objects.get(cantidad=4)
		self.assertEqual(cantidad.cantidad, 4)

	def test_valor_venta(self):
		valor = Venta.objects.get(valor_venta=5)
		self.assertEqual(valor.valor_venta, 5)
		
		

'''
	def test_fecha_venta(self):
		fecha = Venta.objects.get(fecha_venta='2017-10-01')
		self.assertEqual(fecha.fecha_venta, '2017-10-01')
'''		
		