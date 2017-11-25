"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from inventario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	#url(r'^', views.index, name='pagina principal'),
	url(r'^$', views.index, name='pagina principal'),

    url(r'^admin/', admin.site.urls),
    url(r'^', include ('distribuidor.urls')),
    url(r'^', include ('compra.urls')),
    url(r'^', include ('registro.urls')),
    url(r'^', include ('producto.urls')),
    url(r'^', include ('venta.urls')),
    #url(r'^', include ('listarR.urls')),

    url(r'^distribuidor/', include ('distribuidor.urls', namespace='proveedor')),
    url(r'^compra/', include ('compra.urls', namespace='compra')),
    url(r'^producto/', include ('producto.urls', namespace='producto')),
    url(r'^registro/', include ('registro.urls', namespace='registro')),
    url(r'^venta/', include ('venta.urls', namespace='venta')),

    
    

]

#para enviar archivos estaticos al servidor 
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
