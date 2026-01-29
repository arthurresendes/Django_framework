from django.db import models

# Create your models here.

class Estoque(models.Model):
    nome  = models.CharField("Nome",max_length=200)
    preco = models.FloatField("Preco")
    quantidade = models.IntegerField("Quantidade")
    promocao = models.BooleanField("Promocao")
    
    def __str__(self):
        return self.nome