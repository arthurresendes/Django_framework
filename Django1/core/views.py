from django.shortcuts import render
from .models import Produto, Tecnologia

# Create your views here.
def index(request):
    '''
    print(dir(request.user))
    if str(request.user) != 'AnonymousUser':
        teste = f'Logado, usuario: {request.user
        }'
    else:
        teste = 'Não logado'
    '''
    produtos = Produto.objects.all()
    tecnologias = Tecnologia.objects.all()
    
    context ={
        'Projeto': 'Meu primeiro projeto django',
        'produtos': produtos,
        'tecnologias': tecnologias
    }
    return render(request, 'index.html',context)

def contato(request):
    return render(request, 'contato.html')

def tecnologias(request,pk):
    tecno = Tecnologia.objects.get(id=pk)
    context={
        'Tecnologia': 'Python, HTML, CSS, JS e Django',
        'tec': tecno
    }
    return render(request, 'tecnologias.html',context)

def produto(request,pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html',context)