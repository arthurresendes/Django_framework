from django import forms
from .models import Estoque

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['nome', 'preco', 'quantidade', 'promocao']