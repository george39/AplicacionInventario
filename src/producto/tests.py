# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from producto.models import Producto

# Create your tests here.
class ProductoTest(TestCase):
	def setUp(self):
		Producto.objects.create(id_producto='1', nombre_producto='bota', precio_producto=12)
		

	def test_id_producto(self):
		id_producto = Producto.objects.get(id_producto='1')
		self.assertEqual(id_producto.id_producto,'1')

	def test_nombre(self):
		nombre = Producto.objects.get(nombre_producto='bota')
		self.assertEqual(nombre.nombre_producto, 'bota')
		

	def test_precio_venta(self):
		precio = Producto.objects.get(precio_producto=12)
		self.assertEqual(precio.precio_producto, 12)
		