from django.shortcuts import render
from .models import Estoque

# Create your views here.
def index(request):
    context = {
        'estoques': Estoque.objects.all()
    }
    return render(request, 'index.html',context)

def estoque(request,pk):
    stock = Estoque.objects.get(id=pk)
    context = {
        'est': stock
    }
    return render(request, 'estoque.html',context)