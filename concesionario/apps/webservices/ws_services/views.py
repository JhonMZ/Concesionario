# Create your views here.
from django.http import HttpResponse
from concesionario.apps.ventas.models import Carro
from django.core import serializers

def ws_carro_view(request):
	data= serializers.serialize("json",Carro.objects.filter())
	return HttpResponse(data,mimetype= 'application/json')