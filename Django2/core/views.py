from django.shortcuts import render
from .forms import ContatoForm,ProdutoForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def produto(request):
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