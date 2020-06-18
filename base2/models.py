from django.db import models
from stdimage.models import StdImageField # Importação necessária para se utilizar imagens nos models

# __SIGNALS__: Atua sobre os dados antes de salvar no banco de dados
from django.db.models import signals # 'signals' são utilizados para atuar sobre os models antes ou depois dos dados serem gravados no banco de dados
from django.template.defaultfilters import slugify # 'slugify' utilizado para criar uma slug, isto é, pega o titulo da página e coloca-o separado por traços na url da pagina

class Base(models.Model): # É uma classe abstrata, não criada em banco de dados, e que serve apenas de rascunho para outras classes
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)

