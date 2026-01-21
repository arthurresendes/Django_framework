from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.FloatField('Preço')
    quantidade = models.IntegerField('Quantidade')

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=200)
    sobrenome = models.CharField('Sobrenome', max_length=200)
    email = models.EmailField('Email', max_length=100)
    idade = models.IntegerField('Idade')