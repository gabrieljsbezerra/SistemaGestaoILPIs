from django.db import models

class Categoria(models.Model): #Categoria do remedio - foreign key
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo
    
class Remedio(models.Model):
    nome = models.CharField(max_length=60)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) # 1-N
    marca = models.CharField(max_length=40)
    quantidade = models.FloatField()
    preco_compra = models.FloatField()

    def __str__(self):
        return self.nome
    
class Imagem(models.Model):
    imagem = models.ImageField(upload_to="imagem_remedio")
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE)