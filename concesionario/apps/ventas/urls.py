from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('concesionario.apps.ventas.views',
		url(r'^add/carro/$','add_carro_view', name = 'vista_agregar_carro'),
		url(r'^edit/carro/(?P<id_carro>.*)/$','edit_carro_view', name ='vista_editar_carro'),
		url(r'^add/categoria/$','add_categoria_view',name='vista_agregar_categoria'),
		url(r'^edit/categoria/(?P<id_categoria>.*)/$','edit_categoria_view', name ='vista_editar_categoria'),
		url(r'^add/color/$','add_color_view',name = 'vista_agregar_color'),
		url(r'^edit/color/(?P<id_color>.*)/$','edit_color_view', name ='vista_editar_color'),
		url(r'^add/marca/$','add_marca_view',name = 'vista_agregar_marca'),
		url(r'^edit/marca/(?P<id_marca>.*)/$','edit_marca_view', name ='vista_editar_marca'),
		url(r'^add/motor/$','add_motor_view',name = 'vista_agregar_motor'),
		url(r'^edit/motor/(?P<id_motor>.*)/$','edit_motor_view', name ='vista_editar_motor'),
	)