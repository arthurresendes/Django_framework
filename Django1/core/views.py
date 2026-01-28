from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Produto, Tecnologia, Cliente,Estudos

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    tecnologias = Tecnologia.objects.all()
    clientes = Cliente.objects.all()
    estudos = Estudos.objects.all()
    
    context ={
        'Projeto': 'Meu primeiro projeto django',
        'produtos': produtos,
        'tecnologias': tecnologias,
        'clientes': clientes,
        'estudos': estudos
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
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html',context)

def estudo(request,pk):
    estud = get_object_or_404(Estudos, id=pk)
    context = {
        'est': estud
    }
    return render(request, 'estudos.html',context)

def erro404(request,ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html;charset=utf8', status=404)

def erro500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html;charset=utf8', status=500)
