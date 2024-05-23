from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()


class Cards(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    path = models.ImageField(upload_to="imagens/")