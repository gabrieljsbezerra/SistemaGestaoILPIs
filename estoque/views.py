from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Remedio, Imagem
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def add_remedio(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'add_remedio.html', {'categorias': categorias})
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
            draw.text((20, 280), "Projeto Univesp - Sistema ILPIS", (255, 255, 255))
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
        return HttpResponse('foi')