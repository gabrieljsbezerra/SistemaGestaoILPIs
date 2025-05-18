from django.db import models
from idosos.models import Idoso, Responsavel

class Visita(models.Model):
    idoso = models.ForeignKey(Idoso, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Visita de {self.responsavel.nome} para {self.idoso.nome} em {self.data.strftime('%d/%m/%Y')}"
