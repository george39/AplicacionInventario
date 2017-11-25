from django.conf.urls import url, include
from compra.views import indexCompra, compra_view, BuscarCompra



urlpatterns = [
url(r'^$', indexCompra),
url(r'^compras$', compra_view, name='index_compra'),
url(r'^listar$', BuscarCompra.as_view(), name='listar_compra'),
]