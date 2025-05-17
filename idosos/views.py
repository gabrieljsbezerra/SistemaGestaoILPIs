from django.shortcuts import render, redirect, get_object_or_404
from .models import Idoso, Responsavel
from estoque.models import Remedio
from usuarios.models import Users
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required
from .forms import IdosoForm
from .forms import ResponsavelForm

@login_required
def home(request):
    return render(request, 'home.html')
@has_permission_decorator('cadastrar_idoso')
def lista_idosos(request):
    idosos = Idoso.objects.all()
    return render(request, 'idosos/lista_idosos.html', {'idosos': idosos})

@has_permission_decorator('cadastrar_idoso')
def cadastrar_idoso(request):
    if request.method == 'POST':
        form = IdosoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Idoso cadastrado com sucesso!')
            return redirect('lista_idosos')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os campos.')
    else:
        form = IdosoForm()

    return render(request, 'idosos/cadastrar_idoso.html', {'form': form})

@has_permission_decorator('cadastrar_idoso')
def editar_idoso(request, id):
    idoso = get_object_or_404(Idoso, id=id)

    if request.method == 'POST':
        form = IdosoForm(request.POST, request.FILES, instance=idoso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro do idoso atualizado com sucesso!')
            return redirect('lista_idosos')
    else:
        form = IdosoForm(instance=idoso)

    return render(request, 'idosos/editar_idoso.html', {'form': form, 'idoso': idoso})

@has_permission_decorator('cadastrar_idoso')
def excluir_idoso(request, id):
    idoso = get_object_or_404(Idoso, id=id)
    idoso.delete()
    messages.success(request, 'Idoso excluído com sucesso!')
    return redirect('lista_idosos')

@login_required
def cadastrar_responsavel(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_responsaveis')
    else:
        form = ResponsavelForm()
    return render(request, 'idosos/cadastrar_responsavel.html', {'form': form})

@login_required
def lista_responsaveis(request):
    responsaveis = Responsavel.objects.all()
    return render(request, 'idosos/lista_responsaveis.html', {'responsaveis': responsaveis})

@login_required
def editar_responsavel(request, id):
    responsavel = get_object_or_404(Responsavel, id=id)
    if request.method == 'POST':
        form = ResponsavelForm(request.POST, instance=responsavel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Responsável atualizado com sucesso!')
            return redirect('lista_responsaveis')
    else:
        form = ResponsavelForm(instance=responsavel)
    return render(request, 'idosos/editar_responsavel.html', {'form': form, 'responsavel': responsavel})

@login_required
def excluir_responsavel(request, id):
    responsavel = get_object_or_404(Responsavel, id=id)
    responsavel.delete()
    messages.success(request, 'Responsável excluído com sucesso!')
    return redirect('lista_responsaveis')