from django.db import models

# Create your models here.
class Moto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
   
    

class Taller(models.Model):
    nombre_mecanico = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()