from django import forms # Da framework Django, importa-se o seu proprio modulo de formulários para ser usado

# A classe de formulários raiz do Django é a 'Form', que é definida no modulo 'forms' do Django

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    # widget=forms.Textarea() indica que é uma area de texto, portanto deve ser grande
    
    
