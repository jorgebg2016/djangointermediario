from django.contrib import admin
from .models import Produto

@admin.register(Produto) # Usa-se esse decorator para registrar a classe Produto como admin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')

# Register your models here.
