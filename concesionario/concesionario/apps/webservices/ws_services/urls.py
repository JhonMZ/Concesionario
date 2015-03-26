from django.conf.urls.defaults import patterns, url

from django.conf.urls import include
from rest_framework import routers
from concesionario.apps.webservices.ws_services.views import *
router = routers.DefaultRouter()
router.register(r'carros', carro_viewset)
router.register(r'marca', marca_viewset)
router.register(r'color', color_viewset)
router.register(r'motor', motor_viewset)
router.register(r'categoria', categoria_viewset)

urlpatterns = patterns('concesionario.apps.webservices.ws_services.views',
		url(r'^ws/carro/$','ws_carro_view', name = 'vista_json'),
		url(r'^api/', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	)

