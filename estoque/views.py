from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Remedio, Imagem

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
            img = Imagem(imagem = i, remedio=remedio)
            img.save()
        return HttpResponse('foi')