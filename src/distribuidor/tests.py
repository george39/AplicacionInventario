# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from distribuidor.models import Distribuidor

# Create your tests here.
class DistribuidorTest(TestCase):
	def setUp(self):
		Distribuidor.objects.create(nit_distribuidor='2', nombre_distribuidor='jorge', direccion='calle 20', telefono='330')

	def test_nit_proveedor(self):
		nit = Distribuidor.objects.get(nit_distribuidor='2')
		self.assertEqual(nit.nit_distribuidor, '2')
		

	def test_nombre_distribuidor(self):
		nombre = Distribuidor.objects.get(nombre_distribuidor='jorge')
		self.assertEqual(nombre.nombre_distribuidor, 'jorge')

	def test_direccion(self):
		direccion = Distribuidor.objects.get(direccion='calle 20')
		self.assertEqual(direccion.direccion, 'calle 20')

	def test_telefono(self):
		telefono = Distribuidor.objects.get(telefono='330')
		self.assertEqual(telefono.telefono, '330')
		
		
		
