from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['responsavel', 'idoso', 'data', 'horario', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%d-%m-%Y'),
            'horario': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-select'}),
            'idoso': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Corrige exibição da data no campo do formulário (usado no modo edição)
        if self.instance and self.instance.data:
            self.initial['data'] = self.instance.data.strftime('%Y-%m-%d')
