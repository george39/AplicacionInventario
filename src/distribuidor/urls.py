from django.conf.urls import url, include
from distribuidor.views import index, distri_view, DistriUpdate

urlpatterns = [
url(r'^$', index, name='index_distri'),
url(r'^proveedor$', distri_view, name='index_view'),
url(r'^editar/(?P<pk>\d+)/$', DistriUpdate.as_view(), name='distri_editar'),
]