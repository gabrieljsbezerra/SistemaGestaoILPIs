from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator


@has_permission_decorator('cadastrar_usuario')
def cadastrar_usuario(request):
    return render(request, 'cadastrar_usuario.html')
