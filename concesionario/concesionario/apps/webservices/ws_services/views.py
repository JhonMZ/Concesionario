# Create your views here.
from django.http import HttpResponse
from concesionario.apps.ventas.models import *
from .serializer import *
from django.core import serializers
from django.conf.urls import url,include
from rest_framework import routers,serializers,viewsets

def ws_carro_view(request):
	data= serializers.serialize("json",Carro.objects.filter())
	return HttpResponse(data,mimetype= 'application/json')

class  carro_viewset (viewsets.ModelViewSet): 
    queryset =  Carro.objects.all () 
    serializer_class = carro_serializer

class  color_viewset (viewsets.ModelViewSet): 
    queryset =  Color.objects.all () 
    serializer_class = color_serializer

class  categoria_viewset (viewsets.ModelViewSet): 
    queryset =  Categoria.objects.all () 
    serializer_class = categoria_serializer

class  motor_viewset (viewsets.ModelViewSet): 
    queryset =  Motor.objects.all () 
    serializer_class = motor_serializer

class  marca_viewset (viewsets.ModelViewSet): 
    queryset =  Marca.objects.all () 
    serializer_class = marca_serializer