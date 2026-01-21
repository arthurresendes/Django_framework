from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.FloatField('Preço')
    quantidade = models.IntegerField('Quantidade')
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=200)
    sobrenome = models.CharField('Sobrenome', max_length=200)
    email = models.EmailField('Email', max_length=100)
    idade = models.IntegerField('Idade')
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"