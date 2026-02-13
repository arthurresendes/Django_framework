from django.shortcuts import render
from .models import Estoque
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .forms import ProdutoForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {
        'estoques': Estoque.objects.all()
    }
    return render(request, 'index.html',context)

def estoque(request,pk):
    stock = get_object_or_404(Estoque, id=pk)
    context = {
        'est': stock
    }
    return render(request, 'estoque.html',context)


def error404(request,ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html;charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html;charset=utf8', status=500)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = ProdutoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"Produto adicionado com sucesso")
                form  = ProdutoForm()
            else:
                messages.error(request, "Erro ao adicionar")
        else:
            form = ProdutoForm()
        context = {
            'form': form
        }
        return render(request, 'adicionar.html',context)
    else:
        return redirect('index')