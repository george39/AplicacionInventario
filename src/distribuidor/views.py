# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from distribuidor.forms import DistriForm
from django.views.generic import ListView, CreateView, UpdateView 
from django.core.urlresolvers import reverse_lazy
from distribuidor.models import Distribuidor

def index(request):
	return render(request, 'inicio/index.html')
# Create your views here.

def distri_view(request):
	if request.method == 'POST':
		form = DistriForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('proveedor:index_view')
	else:
		form = DistriForm()
	return render(request, 'proveedor/proveedor_form.html', {'form':form})


class DistriUpdate(UpdateView):
	model = Distribuidor
	form_class = DistriForm
	template_name = 'proveedor/registro_form.html'
	success_url = reverse_lazy('proveedor:index_view')

			

