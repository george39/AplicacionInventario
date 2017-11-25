# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.forms import RegistroForm
from.models import Registro
from django.views.generic import ListView, TemplateView
from reportlab.pdfgen import canvas
from django.views.generic import View
from io import BytesIO
from reportlab.lib.pagesizes import A4, cm
from django.views.generic.base import View

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

#import pdfcrowd
#from django.pdf.utileria import render_pdf

# Create your views here.

def indexRegistro(request):
	return render(request, 'inicio/index.html')


def registro_view(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('compra:index_compra')
	else:
		form = RegistroForm()
	return render(request, 'registro/registro_form.html', {'form':form})


class pdf(View):
	
	def get(self, request, *args, **wwargs):
		datos = {'id_registro': 'Id registro',
	    'id_producto' : 'Id producto',
	    'nombre_registro' : 'Nombre', 
	    'cantidad_registro' : 'Cantidad',
	    'fecha_registro' : 'Fecha'}
		pdf = render_pdf('registro/registro_form.html', {'datos':datos})
		return HttpResponse(pdf, content_type='aplication/pdf')


class RegistroList(ListView):
	model = Registro
	template_name = 'registro/registro_list.html'







class ReportePersonasPDF(View):  
     
    #def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        #archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo_django.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        #pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)                
         
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=reporte.pdf'
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        #self.cabecera(pdf)
        y = 600
      
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"PYTHON PIURA")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE PERSONAS")

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Id registro', 'Id producto', 'Nombre registro', 'Cantidad registro', 'Fecha registro')
        #Creamos una lista de tuplas que van a contener a los registros
        detalles = [(registro.id_registro, registro.id_producto, registro.nombre_registro, registro.cantidad_registro, registro.fecha_registro) for registro in Registro.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 3 * cm, 5 * cm, 3 * cm, 5* cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 400)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 40,y)    


'''
def report(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=reporte.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)

	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 22)
	c.drawString(300,750,'Reporte')
	c.setFont('Helvetica', 12)
	#c.drawString(30,735,'Reporte')

	c.setFont('Helvetica-Bold', 12)
	#c.drawString(480,750,"01/11/2017")

	#c.line(460,747,560,747)
	
	styles = getSampleStyleSheet()
	styleBH = styles["Normal"]
	styleBH.alignment = TA_CENTER
	

	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
'''	



