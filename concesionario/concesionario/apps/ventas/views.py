# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from concesionario.apps.ventas.forms import add_carro_form
from concesionario.apps.ventas.forms import edit_carro_form
from concesionario.apps.ventas.forms import add_categoria_form
from concesionario.apps.ventas.forms import edit_categoria_form
from concesionario.apps.ventas.forms import add_color_form
from concesionario.apps.ventas.forms import edit_color_form
from concesionario.apps.ventas.forms import add_marca_form
from concesionario.apps.ventas.forms import edit_marca_form
from concesionario.apps.ventas.forms import add_motor_form
from concesionario.apps.ventas.forms import edit_motor_form
from concesionario.apps.ventas.models import Marca
from concesionario.apps.ventas.models import Carro
from concesionario.apps.ventas.models import Categoria
from concesionario.apps.ventas.models import Color
from concesionario.apps.ventas.models import Motor
from django.http import HttpResponseRedirect

def add_carro_view(request):
	informacion = ""
	if request.method == "POST":#si es post
		formulario = add_carro_form(request.POST, request.FILES)
		informacion = "inicializado"
		if formulario.is_valid():
			p = formulario.save(commit= False)
			p.status = True
			p.save() # Guarda la informacion
			formulario.save_m2m()
			
			informacion= "informacion con datos incorrectos"
		
			return HttpResponseRedirect('/carro/%s'%p.id)
	else:#si es get
		formulario = add_carro_form()
		ctx = {'form':formulario,'informacion':informacion}
		return render_to_response('ventas/add_carro.html', ctx, context_instance = RequestContext(request))

def add_categoria_view(request):
	informacion = ""
	if request.method == "POST":#si es post
		formulario = add_categoria_form(request.POST)
		informacion = "inicializado"
		if formulario.is_valid():
			p = formulario.save(commit= False)
			p.status = True
			p.save() # Guarda la informacion
			formulario.save_m2m()
			
			informacion= "informacion con datos incorrectos"
		
			return HttpResponseRedirect('/categorias/page/1')
	else:#si es get
		formulario = add_categoria_form()
		ctx = {'form':formulario,'informacion':informacion}
		return render_to_response('ventas/add_categoria.html', ctx, context_instance = RequestContext(request))

def edit_categoria_view(request, id_categoria):
	info = ""
	carro = Categoria.objects.get(id = id_categoria)
	if request.method == "POST":
		formulario = edit_categoria_form(request.POST, request.FILES, instance = carro)
		if formulario.is_valid():
			edit_categoria = formulario.save(commit = False)
			formulario.save_m2m()
			edit_categoria.status = True			
			edit_categoria.save()
			info = "se guardo satisfactoriamente"				
			return HttpResponseRedirect('/categorias/page/1')
	else:
		formulario = edit_categoria_form (instance = carro)
	ctx = {'form':formulario, 'carro':info, 'carro_id':carro}
	return render_to_response('ventas/edit_categoria.html',ctx ,context_instance = RequestContext(request))

def edit_carro_view(request, id_carro):
	info = ""
	carro = Carro.objects.get(id = id_carro)
	if request.method == "POST":
		formulario = edit_carro_form(request.POST, request.FILES, instance = carro)
		if formulario.is_valid():
			edit_carro = formulario.save(commit = False)
			formulario.save_m2m()
			edit_carro.status = True			
			edit_carro.save()
			info = "se guardo satisfactoriamente"				
			return HttpResponseRedirect('/carro/%s'%carro.id)
	else:
		formulario = edit_carro_form (instance = carro)
	ctx = {'form':formulario, 'carro':info, 'carro_id':carro}
	return render_to_response('ventas/edit_carro.html',ctx ,context_instance = RequestContext(request))


def administrador_view(request):
	return render_to_response('ventas/admin.html',context_instance = RequestContext(request))

def add_color_view(request):
	informacion = ""
	if request.method == "POST":#si es post
		formulario = add_color_form(request.POST)
		informacion = "inicializado"
		if formulario.is_valid():
			p = formulario.save(commit= False)
			p.status = True
			p.save() # Guarda la informacion
			formulario.save_m2m()
			
			informacion= "informacion con datos incorrectos"
		
			return HttpResponseRedirect('/colores/page/1')
	else:#si es get
		formulario = add_color_form()
		ctx = {'form':formulario,'informacion':informacion}
		return render_to_response('ventas/add_color.html', ctx, context_instance = RequestContext(request))

def edit_color_view(request, id_color):
	info = ""
	color = Color.objects.get(id = id_color)
	if request.method == "POST":
		formulario = edit_color_form(request.POST, instance = color)
		if formulario.is_valid():
			edit_color = formulario.save(commit = False)
			formulario.save_m2m()
			edit_color.status = True			
			edit_color.save()
			info = "se guardo satisfactoriamente"				
			return HttpResponseRedirect('/colores/page/1')
	else:
		formulario = edit_color_form (instance = color)
	ctx = {'form':formulario, 'color':info, 'color_id':color}
	return render_to_response('ventas/edit_color.html',ctx ,context_instance = RequestContext(request))

def add_marca_view(request):
	informacion = ""
	if request.method == "POST":#si es post
		formulario = add_marca_form(request.POST)
		informacion = "inicializado"
		if formulario.is_valid():
			p = formulario.save(commit= False)
			p.status = True
			p.save() # Guarda la informacion
			formulario.save_m2m()
			
			informacion= "informacion con datos incorrectos"
		
			return HttpResponseRedirect('/marcas/page/1')
	else:#si es get
		formulario = add_marca_form()
		ctx = {'form':formulario,'informacion':informacion}
		return render_to_response('ventas/add_marca.html', ctx, context_instance = RequestContext(request))

def edit_marca_view(request, id_marca):
	info = ""
	marca = Marca.objects.get(id = id_marca)
	if request.method == "POST":
		formulario = edit_marca_form(request.POST, instance = marca)
		if formulario.is_valid():
			edit_marca = formulario.save(commit = False)
			formulario.save_m2m()
			edit_marca.status = True			
			edit_marca.save()
			info = "se guardo satisfactoriamente"				
			return HttpResponseRedirect('/marcas/page/1')
	else:
		formulario = edit_marca_form (instance = marca)
	ctx = {'form':formulario, 'marca':info, 'marca_id':marca}
	return render_to_response('ventas/edit_marca.html',ctx ,context_instance = RequestContext(request))

def add_motor_view(request):
	informacion = ""
	if request.method == "POST":#si es post
		formulario = add_motor_form(request.POST)
		informacion = "inicializado"
		if formulario.is_valid():
			p = formulario.save(commit= False)
			p.status = True
			p.save() # Guarda la informacion
			formulario.save_m2m()
			
			informacion= "informacion con datos incorrectos"
		
			return HttpResponseRedirect('/motores/page/1')
	else:#si es get
		formulario = add_motor_form()
		ctx = {'form':formulario,'informacion':informacion}
		return render_to_response('ventas/add_motor.html', ctx, context_instance = RequestContext(request))

def edit_motor_view(request, id_motor):
	info = ""
	motor = Motor.objects.get(id = id_motor)
	if request.method == "POST":
		formulario = edit_motor_form(request.POST, instance = motor)
		if formulario.is_valid():
			edit_motor = formulario.save(commit = False)
			formulario.save_m2m()
			edit_motor.status = True			
			edit_motor.save()
			info = "se guardo satisfactoriamente"				
			return HttpResponseRedirect('/motores/page/1')
	else:
		formulario = edit_motor_form (instance = motor)
	ctx = {'form':formulario, 'motor':info, 'motor_id':motor}
	return render_to_response('ventas/edit_motor.html',ctx ,context_instance = RequestContext(request))
