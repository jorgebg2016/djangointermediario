from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

# Create your views here.
# Definiremos três views: A Index que carregará os dados, a pagina de Contatos, e uma view de Formulários

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        # print(f'Post: {request.POST}') # Printa a requisição que foi enviada pelo metodo POST
        if form.is_valid(): # Retorna True se o formulário não tem erros, isto é, se o formulário tem todos os seus campos preenchidos
            form.send_mail() # Envia um e-mail em resposta do usuario que contactou e colocou seus dados no formulário
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm() #Limpando o formulário
        else:
            messages.error(request, 'Erro ao enviar a mensagem')

    context = {
        'form':form
    }
    return render(request, 'contato.html', context)


def produto(request):
    print(f'usuario: {request.user}')
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                prod = form.save(commit=True)
                messages.success(request, f'Produto {prod.nome} salvo com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto.')
        else:
            form = ProdutoModelForm()    
        context = {'form':form}
        return render(request, 'produto.html', context)
    else:
        return redirect('index')
