from django.contrib import admin
from .models import Produto,Cliente,Tecnologia,Estudos

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','quantidade')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email','idade')
    
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nomePessoa', 'nomeTec', 'tempo')
    
class EstudosAdmin(admin.ModelAdmin):
    list_display = ('diaEstudo', 'materiaEstudo')

admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Tecnologia,TecnologiaAdmin)
admin.site.register(Estudos,EstudosAdmin)
