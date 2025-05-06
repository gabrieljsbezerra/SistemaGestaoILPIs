from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from rolepermissions.roles import assign_role
from django.contrib import messages

@has_permission_decorator('cadastrar_usuario')
def cadastrar_usuario(request):
    if request.method == "GET":
        usuarios = Users.objects.filter(cargo="U") # Para listar os usuarios, busco no banco de dados como um select com where
        return render(request, 'cadastrar_usuario.html', {'usuarios': usuarios})
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Implementar as messages do django 
            return HttpResponse('E-mail existente')

        user = Users.objects.create_user(
            first_name=nome,
            last_name=sobrenome,
            username=email,
            email=email,
            password=senha,
            cargo="U"
        )
        assign_role(user, 'usuario')
        # TODO: Redirecionar para tela de login com mensagem de sucesso
        return HttpResponse('Conta criada com sucesso!')
    
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(
            username=login,
            password=senha
        )
        if not user:
            # TODO: Redirecionar para login com mensagem de erro
            return HttpResponse('Usuario invalido!')
            
        auth.login(request, user)
        return HttpResponse('Usuario Logado!')
    
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_usuario')
def excluir_usuario(request, id):
    usuario = get_object_or_404(Users, id=id) #Busca no banco de dados a info... se n existir retorna erro 404
    usuario.delete()
    messages.add_message(request, messages.SUCCESS, 'Usuário deletado com sucesso!')
    return redirect(reverse('cadastrar_usuario'))