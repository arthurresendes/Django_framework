from django.shortcuts import render
from .models import Produto

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
    
    context ={
        'Projeto': 'Meu primeiro projeto django',
        'produtos': produtos
    }
    return render(request, 'index.html',context)

def contato(request):
    return render(request, 'contato.html')

def tecnologias(request):
    context={
        'Tec': 'Python, HTML, CSS, JS e Django'
    }
    return render(request, 'tecnologias.html',context)

def produto(request,pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html',context)