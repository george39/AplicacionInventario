# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Compra
from.forms import CompraForm
from django.views.generic import TemplateView
# Create your views here.

def indexCompra(request):
	return render(request, 'inicio/index.html')


def compra_view(request):
	if request.method == 'POST':
		form = CompraForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('compra:index_compra')
	else:
		form = CompraForm()
	return render(request, 'compra/form_compras.html', {'form':form})


class BuscarCompra(TemplateView):
	#model = Compra
	template_name = 'compra/compra_buscar.html'

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		buscar_compra = Compra.objects.filter(codigo_compra=4546)
		print buscar_compra
		return render(request, 'compra/compra_buscar.html')

