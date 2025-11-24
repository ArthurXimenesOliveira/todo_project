from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

class Viagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    destino = models.CharField(max_length=100)
    data = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.destino
