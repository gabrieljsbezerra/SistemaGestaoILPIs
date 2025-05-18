from django.shortcuts import render, redirect, get_object_or_404
from .models import Visita
from .forms import VisitaForm
from django.db.models import Q
from datetime import datetime

def lista_visitas(request):
    busca = request.GET.get('busca', '')
    visitas = Visita.objects.all()

    if busca:
        filtros = (
            Q(idoso__nome__icontains=busca) |
            Q(responsavel__nome__icontains=busca) |
            Q(observacoes__icontains=busca)
        )

        try:
            data_busca = datetime.strptime(busca, "%d/%m/%Y").date()
            filtros |= Q(data=data_busca)
        except ValueError:
            try:
                data_busca = datetime.strptime(busca, "%Y-%m-%d").date()
                filtros |= Q(data=data_busca)
            except ValueError:
                pass

        visitas = visitas.filter(filtros)

    return render(request, 'visitas/lista_visitas.html', {'visitas': visitas, 'busca': busca})
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
