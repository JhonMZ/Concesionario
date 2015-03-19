from django import forms
from concesionario.apps.ventas.models import Carro
from concesionario.apps.ventas.models import Categoria
from concesionario.apps.ventas.models import Color
from concesionario.apps.ventas.models import Marca
from concesionario.apps.ventas.models import Motor

class add_carro_form(forms.ModelForm):
	class Meta:
		model 	=  Carro

class edit_carro_form(forms.ModelForm):
	class Meta:
		model = Carro
			
class  add_categoria_form(forms.ModelForm):
	class Meta:
		model = Categoria

class edit_categoria_form(forms.ModelForm):
	class Meta:
		model = Categoria

class add_color_form(forms.ModelForm):
	class Meta:
		model= Color

class edit_color_form(forms.ModelForm):
	class Meta:
		model=Color

class add_marca_form(forms.ModelForm):
	class Meta:
		model= Marca
		
class edit_marca_form(forms.ModelForm):
	class Meta:
		model= Marca

class add_motor_form(forms.ModelForm):
	class Meta:
		model= Motor
		
class edit_motor_form(forms.ModelForm):
	class Meta:
		model= Motor