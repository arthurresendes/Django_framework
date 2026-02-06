from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def produto(request):
    return render(request, 'produto.html')

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