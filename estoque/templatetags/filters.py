from django import template
from estoque.models import Imagem
register = template.Library()

@register.filter(name='get_first_image')
def  get_first_image(remedio):
    imagem = Imagem.objects.filter(remedio=remedio).first()
    if imagem:
        return imagem.imagem.url
    else:
        return False