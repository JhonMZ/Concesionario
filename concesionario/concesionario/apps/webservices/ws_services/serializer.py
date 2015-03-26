from rest_framework import serializers
from concesionario.apps.ventas.models import *

class carro_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Carro
		fields = ('url','carnombre','color','marca','motor','categoria','precio','modelo','imagen',)

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('url','marnombre',)

class categoria_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('url','catnombre',)

class color_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Color
		fields = ('url','nombrecolor','colhex',)

class motor_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Motor
		fields = ('url','motnombre','cilindraje','tipomotor',)