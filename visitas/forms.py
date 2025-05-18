from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['responsavel', 'idoso', 'data', 'horario', 'observacoes']
