from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('concesionario.apps.webservices.ws_services.views',
		url (r'^ws/carro/$','ws_carro_view', name = 'vista_json'),
	)

