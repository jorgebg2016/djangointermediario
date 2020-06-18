from django import forms # Da framework Django, importa-se o seu proprio modulo de formulários para ser usado
from django.core.mail.message import EmailMessage # Importações necessarias para se utilizar o pacote de emails do django

from .models import Produto


# A classe de formulários raiz do Django é a 'Form', que é definida no modulo 'forms' do Django

class ContatoForm(forms.Form): # Estende Form, logo é uma classe de formulário
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    # widget=forms.Textarea() indica que é uma area de texto, portanto deve ser 
    
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Olá {nome}, responderemos em breve!'

        mail = EmailMessage(
            subject = 'E-mail resposta enviado pelo sistema base2',
            body = conteudo,
            from_email = 'base2@sistemapp.com.br',
            to=[str(email),], # Define para quem o e-mail será respondido
            headers={'replay-to': 'base2@sistemapp.com.br'}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm): # Estende ModelForm, logo é uma classe de ModelForm
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
    
