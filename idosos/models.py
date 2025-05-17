from django.db import models
from estoque.models import Remedio  # Importa o modelo existente de remédios

class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Idoso(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.TextField()
    foto = models.ImageField(upload_to='fotos_idosos/', blank=True, null=True)  # NOVO CAMPO

    responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='idosos'
    )
    remedios = models.ManyToManyField(
        Remedio,
        blank=True,
        related_name='idosos_em_uso'
    )
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome