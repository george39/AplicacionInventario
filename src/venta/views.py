# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from.models import Venta 
from.forms import VentaForm

# Create your views here.

def indexVenta(request):
	return render(request, 'inicio/index.html')


def venta_view(request):
	if request.method == 'POST':
		form = VentaForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('compra:index_compra')
	else:
		form = VentaForm()
	return render(request, 'venta/venta_form.html', {'form':form})