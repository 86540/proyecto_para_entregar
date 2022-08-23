from django.db import models

# Create your models here.
class cadena(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)

class fecha(models.Model):
    nombre=models.CharField(max_length=40)
    entrega=models.DateField()

class numero(models.Model):
    nombre=models.CharField(max_length=40)
    number=models.IntegerField()

