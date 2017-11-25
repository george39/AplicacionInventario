# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from registro.models import Registro


# Create your tests here.
class RegistroTest(TestCase):
	def setUp(self):
		Registro.objects.create(id_registro='1', nombre_registro='montera', cantidad_registro=2, fecha_registro='2017-10-22')

	def test_registro_id(self):
		registro = Registro.objects.get(id_registro='1')
		self.assertEqual(registro.id_registro, '1')

	def test_nombre_registro(self):
			nombre = Registro.objects.get(nombre_registro='montera')
			self.assertEqual(nombre.nombre_registro, 'montera')	

	def test_cantidad_registro(self):
		cantidad = Registro.objects.get(cantidad_registro=2)
		self.assertEqual(cantidad.cantidad_registro, 2)


'''
	def test_fecha_registro(self):
		fecha = Registro.objects.get(fecha_registro='2017-10-22')
		self.assertEqual(fecha.fecha_registro,'2017-10-22')
'''
			