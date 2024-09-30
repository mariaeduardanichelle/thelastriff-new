from django.db import models
from django.contrib.auth.models import User


class Guitarra(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    preco = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return f'{self.marca} - {self.modelo}'
    

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    guitarra = models.ForeignKey(Guitarra, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} - {self.guitarra}'
