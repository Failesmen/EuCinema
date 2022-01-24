from pyexpat import model
from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name
