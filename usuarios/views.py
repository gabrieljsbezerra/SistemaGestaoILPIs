from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users

@has_permission_decorator('cadastrar_usuario')
def cadastrar_usuario(request):
    if request.method == "GET":
        return render(request, 'cadastrar_usuario.html')
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Implementar as messages do django 
            return HttpResponse('E-mail existente')

        user = Users.objects.create_user(
            username=email,
            email=email,
            password=senha,
            cargo="G"
        )
        # TODO: Redirecionar para tela de login com mensagem de sucesso
        return HttpResponse('Conta criada com sucesso!')