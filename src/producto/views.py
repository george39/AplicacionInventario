# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Producto
from.forms import ProductoForm

# Create your views here.
def indexProducto(request):
	return render(request, 'inicio/index.html')


def producto_view(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('compra:index_compra')
	else:
		form = ProductoForm()
	return render(request, 'producto/producto_form.html', {'form':form})