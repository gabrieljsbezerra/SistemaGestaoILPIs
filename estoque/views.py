from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria

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
        imagens = request.FILES
        print(imagens)
        return HttpResponse('foi')