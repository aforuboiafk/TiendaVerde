from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField() 
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Carro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carros') 
    productos = models.ManyToManyField(Producto, related_name='carros')
    total = models.IntegerField()
    estado = models.CharField(max_length=(20))  

    def __str__(self):
        return f'Carro de {self.usuario.username}'