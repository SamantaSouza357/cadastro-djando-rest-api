from django.db import models

# Create your models here.
from django.db.models import CharField


class Aluno(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='nome'
    )
    idade = models.IntegerField(
        verbose_name='idade'
    )
    email = models.EmailField(
        max_length=50,
        verbose_name='email'
    )

    def __str__(self):
        return self.nome

