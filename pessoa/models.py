from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe

class Localizacao(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


class Sobrevivente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=2)
    pontos= models.IntegerField()
    denuncias = models.IntegerField()
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    infectado = models.BooleanField(default=False)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'


    def __str__(self):
        return self.nome
