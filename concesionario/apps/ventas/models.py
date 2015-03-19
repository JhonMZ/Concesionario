from django.db import models

from django.db import models

# Create your models here.

class Color(models.Model):
	nombrecolor = models.CharField(max_length = 15)	
	colhex 		= models.CharField(max_length = 7)
	def __unicode__ (self):
		return self.nombrecolor

class Motor(models.Model):
	motnombre 	= models.CharField(max_length = 15)
	cilindraje	= models.CharField(max_length = 15)
	tipomotor	= models.CharField(max_length = 15)
	def __unicode__ (self):
		return self.motnombre

class Marca(models.Model):
	marnombre = models.CharField(max_length = 20)
	#logo =
	def __unicode__ (self):
		return self.marnombre

class Categoria(models.Model):
 	catnombre = models.CharField(max_length = 20)
 	def __unicode__ (self):
		return self.catnombre

class Carro(models.Model):
	def url(self, filename):
		ruta = "MultimediaData/Carro/%s/%s"%(self.carnombre, str(filename))
		return ruta
	carnombre	= models.CharField(max_length = 20)
	color 		= models.ManyToManyField(Color)
	marca 		= models.ForeignKey(Marca)
	motor 		= models.ForeignKey(Motor)
	categoria 	= models.ManyToManyField(Categoria)
	precio 		= models.IntegerField()
	modelo 		= models.CharField(max_length = 6)
	imagen 		= models.ImageField(upload_to = url, null = True, blank = True)
	def __unicode__ (self):
		return self.carnombre
	