from django.conf.urls import url, include 
from venta.views import indexVenta, venta_view

urlpatterns = [
url(r'^$', indexVenta),
url(r'^ventas$', venta_view, name='index_venta'),
]
