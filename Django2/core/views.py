from django.shortcuts import render
from .forms import ContatoForm,ProdutoForm
from django.contrib import messages
from .models import Produto
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html',context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = ProdutoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"Produto salvo")
                form  = ProdutoForm()
            else:
                messages.error(request, "Erro ao enviar e-mail")
        else:
            form = ProdutoForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html',context)
    else:
        return redirect('index')

def contato(request):
    form = ContatoForm()
    
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, "E-mail enviado com sucesso")
            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar e-mail")
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)