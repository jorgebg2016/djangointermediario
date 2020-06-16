from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

# Create your views here.
# Definiremos três views: A Index que carregará os dados, a pagina de Contatos, e uma view de Formulários

def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        print(f'Post: {request.POST}')
        if form.is_valid(): # Retorna True se o formulário não tem erros, isto é, se o formulário tem todos os seus campos preenchidos
            nome = form.cleaned_data['nome']         #
            email = form.cleaned_data['email']       # cleaned_data['name_field_input']: Pega os dados dos campos do formulário
            assunto = form.cleaned_data['assunto']   #
            mensagem = form.cleaned_data['mensagem'] #

            print('___Mensagem enviada___')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm() #Limpando o formulário
        else:
            messages.error(request, 'Erro ao enviar a mensagem')

    context = {
        'form':form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')
