from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto, Tecnologia, Cliente

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    tecnologias = Tecnologia.objects.all()
    clientes = Cliente.objects.all()
    
    context ={
        'Projeto': 'Meu primeiro projeto django',
        'produtos': produtos,
        'tecnologias': tecnologias,
        'clientes': clientes
    }
    return render(request, 'index.html',context)

def cliente(request,pk):
    #cliente = Cliente.objects.get(id=pk)
    cliente = get_object_or_404(Cliente, id=pk)
    context = {
        'clie': cliente
    }
    return render(request, 'contato.html',context)

def tecnologias(request,pk):
    tecno = get_object_or_404(Tecnologia,id=pk)
    context={
        'Tecnologia': 'Python, HTML, CSS, JS e Django',
        'tec': tecno
    }
    return render(request, 'tecnologias.html',context)

def produto(request,pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html',context)
