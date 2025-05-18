from django.shortcuts import render, redirect, get_object_or_404
from .models import Visita
from .forms import VisitaForm

def lista_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'visitas/lista_visitas.html', {'visitas': visitas})

def nova_visita(request):
    form = VisitaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_visitas')
    return render(request, 'visitas/form_visita.html', {'form': form})

def editar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    form = VisitaForm(request.POST or None, instance=visita)
    if form.is_valid():
        form.save()
        return redirect('lista_visitas')
    return render(request, 'visitas/form_visita.html', {'form': form})

def excluir_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    visita.delete()
    return redirect('lista_visitas')
