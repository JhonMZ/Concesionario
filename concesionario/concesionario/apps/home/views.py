# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from concesionario.apps.ventas.models import Carro
from concesionario.apps.ventas.models import Categoria
from concesionario.apps.ventas.models import Color 
from concesionario.apps.ventas.models import Marca
from concesionario.apps.ventas.models import Motor
from concesionario.apps.home.forms import contact_form
from concesionario.apps.home.forms import Login_form
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.mail import EmailMultiAlternatives

def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))
def single_product_view(request, id_carro):
	carro = Carro.objects.get(id = id_carro)
	ctx = {'carro':carro}
	return render_to_response('home/single_producto.html', ctx, context_instance = RequestContext(request))

	
	return render_to_response('home/color.html',ctx,context_instance = RequestContext(request))
def carro_view(request, pagina):
	ca = Carro.objects.filter()#SELECT * FROM Categoria Where status = True
	paginator = Paginator(ca,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		carros = paginator.page(page)
	except (EmptyPage,InvalidPage):
		carros = paginator.page(paginator.num_pages)
	ctx = {'carros':carros}
	
	return render_to_response('home/carros.html',ctx,context_instance = RequestContext(request))

def categorias_view(request, pagina):
	ca = Categoria.objects.filter()#SELECT * FROM Categoria Where status = True
	paginator = Paginator(ca,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		categoria = paginator.page(page)
	except (EmptyPage,InvalidPage):
		categoria = paginator.page(paginator.num_pages)
	ctx = {'categoria':categoria}
	
	return render_to_response('home/categorias.html',ctx,context_instance = RequestContext(request))



def contact_view(request):
	info_enviado = False #Definir si se envio informacion o no
	email = ""
	title = ""
	text  = ""
	if request.method == "POST": #evalua si el metodo fue POST
		formulario = contact_form(request.POST)#instancia del formulario con los datos ingresados
		if formulario.is_valid(): #evalua si el formulario es valido
			info_enviado = True #la informacion se envio correctamente
			email = formulario.cleaned_data['correo'] #copia el correo ingresado en email
			title = formulario.cleaned_data['titulo'] #copia el titulo infresado en title
			text  = formulario.cleaned_data['texto']  #copia el texto ingresado en text
			
			#bloque configuracion de envio por gmail
			to_admin = 'kaoxdc@gmail.com'
			html_content = "informacion recibida de %s <br> ---Mensaje---<br>%s"%(email,text)
			msg = EmailMultiAlternatives('correo de contacto', html_content, 'from@server.com',[to_admin])
			msg.attach_alternative(html_content, 'text/html')#definimos el contenido como html
			msg.send()#enviamos el correo
			#fin bloque

	else: #si no fue POST entonces fue el metodo get mostrata un formulario vacio
		formulario = contact_form() #creacion del formulario vacio

	ctx = {'form':formulario, 'email':email, "title":title, "text":text, "info_enviado":info_enviado }
	return render_to_response('home/contacto.html', ctx, context_instance = RequestContext(request))

	

def about_view(request):
	return render_to_response('home/about.html', context_instance = RequestContext(request))

def login_view (request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form':formulario, 'mensaje':mensaje}
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def administrador_view(request):
	return render_to_response('home/admin.html',context_instance = RequestContext(request))

def colores_view(request, pagina):
	ca = Color.objects.filter()#SELECT * FROM Categoria Where status = True
	paginator = Paginator(ca,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		color = paginator.page(page)
	except (EmptyPage,InvalidPage):
		color = paginator.page(paginator.num_pages)
	ctx = {'color':color}
	
	return render_to_response('home/colores.html',ctx,context_instance = RequestContext(request))

def marcas_view(request, pagina):
	ca = Marca.objects.filter()#SELECT * FROM Categoria Where status = True
	paginator = Paginator(ca,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		marca = paginator.page(page)
	except (EmptyPage,InvalidPage):
		marca = paginator.page(paginator.num_pages)
	ctx = {'marca':marca}
	
	return render_to_response('home/marcas.html',ctx,context_instance = RequestContext(request))

def motores_view(request, pagina):
	ca = Motor.objects.filter()#SELECT * FROM Categoria Where status = True
	paginator = Paginator(ca,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		motor = paginator.page(page)
	except (EmptyPage,InvalidPage):
		motor = paginator.page(paginator.num_pages)
	ctx = {'motor':motor}
	
	return render_to_response('home/motores.html',ctx,context_instance = RequestContext(request))


	
