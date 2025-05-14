from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Remedio, Imagem
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import get_object_or_404

@has_permission_decorator('cadastrar_medicamentos')
def add_remedio(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        remedios = Remedio.objects.all()
        return render(request, 'add_remedio.html', {'categorias': categorias, 'remedios': remedios})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        marca = request.POST.get('marca')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')

        #salvando e atribuindo no DB
        remedio = Remedio(nome=nome, categoria_id=categoria, marca=marca, quantidade=quantidade, preco_compra=preco_compra)
        remedio.save()

        #salvando cada imagem
        for i in request.FILES.getlist('imagens'):
            name = f'{date.today()}-{remedio.id}.jpg'
            img = Image.open(i)
            img = img.convert('RGB')
            img = img.resize((300, 300))
            draw = ImageDraw.Draw(img)
            draw.text((20, 280), "Projeto Univesp - Sistema ILPIS", (000, 000, 000))
            output = BytesIO() #recebe os bytes da img
            img.save(output, format="JPEG", quality=100)
            output.seek(0) #faz o ponteiro apontar para o inicio do arquivo
            img_final = InMemoryUploadedFile( #associando a um tipo de memoria para salvar
                output,
                'ImageField',
                name,
                'image/jpeg',
                sys.getsizeof(output),
                None
            )
            img_dj = Imagem(imagem = img_final, remedio=remedio)
            img_dj.save()
        messages.add_message(request, messages.SUCCESS, 'Medicamento cadastrado com sucesso!')
        return redirect(reverse('add_remedio'))
    
@has_permission_decorator('cadastrar_medicamentos')
def editar_remedio(request, id):
    remedio = get_object_or_404(Remedio, id=id)

    if request.method == "GET":
        categorias = Categoria.objects.all()
        imagens = Imagem.objects.filter(remedio=remedio)
        return render(request, 'editar_remedio.html', {
            'remedio': remedio,
            'categorias': categorias,
            'imagens': imagens
        })

    elif request.method == "POST":
        remedio.nome = request.POST.get('nome')
        remedio.categoria_id = request.POST.get('categoria')
        remedio.marca = request.POST.get('marca')
        try:
            remedio.quantidade = float(request.POST.get('quantidade', 0))
        except (ValueError, TypeError):
            remedio.quantidade = 0

        try:
            remedio.preco_compra = float(request.POST.get('preco_compra', 0))
        except (ValueError, TypeError):
            remedio.preco_compra = 0
        remedio.save()

        for i in request.FILES.getlist('imagens'):
            name = f'{date.today()}-{remedio.id}.jpg'
            img = Image.open(i)
            img = img.convert('RGB')
            img = img.resize((300, 300))
            draw = ImageDraw.Draw(img)
            draw.text((20, 280), "Projeto Univesp - Sistema ILPIS", (0, 0, 0))
            output = BytesIO()
            img.save(output, format="JPEG", quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(
                output,
                'ImageField',
                name,
                'image/jpeg',
                sys.getsizeof(output),
                None
            )
            nova_img = Imagem(imagem=img_final, remedio=remedio)
            nova_img.save()

        messages.success(request, 'Medicamento atualizado com sucesso!')
        return redirect(reverse('editar_remedio', args=[remedio.id]))
    
def excluir_remedio(request, id):
    remedio = get_object_or_404(Remedio, id=id)
    remedio.delete()
    messages.success(request, 'Remédio excluído com sucesso.')
    return redirect('add_remedio')  # ou a URL para a lista de remédios