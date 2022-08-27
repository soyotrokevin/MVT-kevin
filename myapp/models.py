from pyexpat import model
from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=128)
    parentesco = models.Charfield (max_length=64)
    fecha_nacimiento = models.DateField()
    cant_patas = models.IntegerField()

class Salud(models.Model):
    pass

