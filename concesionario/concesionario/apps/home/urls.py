from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('concesionario.apps.home.views',
	url(r'^$','index_view', name = 'vista_principal'),
	url(r'^carros/page/(?P<pagina>.*)/$','carro_view', name = 'vista_carros'),
	url(r'^carro/(?P<id_carro>.*)/$','single_product_view', name = 'vista_single_producto'),
	url(r'^contacto/$','contact_view',name='vista_contacto'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
	url(r'^categorias/page/(?P<pagina>.*)/$','categorias_view', name = 'vista_categorias'),
	url(r'^colores/page/(?P<pagina>.*)/$','colores_view', name = 'vista_colores'),
	url(r'^marcas/page/(?P<pagina>.*)/$','marcas_view', name = 'vista_marcas'),
	url(r'^motores/page/(?P<pagina>.*)/$','motores_view', name = 'vista_motores'),
	url(r'^administrador','administrador_view',name= 'vista_administrador'),
	)
