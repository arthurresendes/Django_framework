from django.shortcuts import render

# Create your views here.
def index(request):
    # print(dir(request.user))
    if str(request.user) != 'AnonymousUser':
        teste = f'Logado, usuario: {request.user
        }'
    else:
        teste = 'Não logado'

    context ={
        'Projeto': 'Meu primeiro projeto django',
        'logado': teste
    }
    return render(request, 'index.html',context)

def contato(request):
    return render(request, 'contato.html')

def tecnologias(request):
    context={
        'Tec': 'Python, HTML, CSS, JS e Django'
    }
    return render(request, 'tecnologias.html',context)