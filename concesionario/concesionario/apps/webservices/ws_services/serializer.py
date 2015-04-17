from rest_framework import *
from concesionario.apps.ventas.models import *




class color_serializer(serializers.ModelSerializer):
	
	class Meta:
		model = Color
		fields = ('nombrecolor','colhex',)

class carro_serializer(serializers.ModelSerializer):
	marca = serializers.SlugRelatedField(slug_field='marnombre', read_only=True)
	color = serializers.SlugRelatedField(many=True, read_only=True, slug_field='colhex')
	categoria = serializers.SlugRelatedField(many=True, read_only=True, slug_field='catnombre')
	class Meta:

		model = Carro
		fields = ('carnombre','color','marca','motor','categoria','precio','modelo','imagen',)
	


class marca_serializer(serializers.ModelSerializer):
	class Meta:
		model = Marca
		fields = ('marnombre',)

class categoria_serializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('catnombre',)

class motor_serializer(serializers.ModelSerializer):
	class Meta:
		model = Motor
		fields = ('motnombre','cilindraje','tipomotor',)