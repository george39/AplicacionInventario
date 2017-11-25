from django.conf.urls import url 
from producto.views import indexProducto, producto_view

urlpatterns = [
url(r'^$', indexProducto),
url(r'^productos$', producto_view, name='index_producto'),
]