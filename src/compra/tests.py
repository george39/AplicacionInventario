# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import unittest
from compra.models import Compra

# Create your tests here.
class CompraTest(TestCase):
	def setUp(self):
		Compra.objects.create(codigo_compra="1", cantidad=2, valor_compra=20)


	def test_codigo_compra(self):
		codigo = Compra.objects.get(codigo_compra='1')
		self.assertEqual(codigo.codigo_compra,'1')
		
	def test_cantidad_compra(self):
		cantidad = Compra.objects.get(cantidad=2)
		self.assertEqual(cantidad.cantidad, 2)

	def test_valor_compra(self):
		valor = Compra.objects.get(valor_compra=20)
		self.assertEqual(valor.valor_compra,20)
		
		


