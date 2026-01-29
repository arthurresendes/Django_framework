from django.contrib import admin
from .models import Estoque

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','quantidade','promocao')


admin.site.register(Estoque,EstoqueAdmin)
