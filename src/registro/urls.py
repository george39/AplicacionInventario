from django.conf.urls import url, include
#from registro.views import index, RegistroList
from django.views.generic import ListView, TemplateView


from.views import indexRegistro, registro_view, RegistroList, pdf, ReportePersonasPDF

urlpatterns = [
url(r'^$', indexRegistro, name='index'),
url(r'^registros$', registro_view, name='index_compra'),
url(r'^listarcompra$', RegistroList.as_view(), name='registro_listar'),
url(r'^exportar$', pdf.as_view(), name='reporte'),
#url(r'^reporte$', report, name='reporte_registro'),
url(r'^pdf/$', (ReportePersonasPDF.as_view()), name="pdf"),
#url(r'^mipdf/$', PDFView.as_view(template_name='registro_list.html'), name='mipdf'),


] 