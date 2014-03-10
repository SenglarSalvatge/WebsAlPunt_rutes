# -*- encoding: utf-8 -*-
from django.db import models
from usuaris.models import Perfil

class Comentari(models.Model):
    comentari = models.CharField(max_length=800)
    post = models.ForeignKey('posts.Post', related_name="RutatoComentari")
    perfil = models.ForeignKey(Perfil, related_name="comentariUsuari")
    
    class Meta:
        app_label = 'socials'

class Puntuacio(models.Model):
    
    PUNTUACIO_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    puntuacio = models.IntegerField( choices=PUNTUACIO_CHOICES, help_text="Puntuació")
    post = models.ForeignKey('posts.Post', related_name="RutatoPuntuacio")
    perfil = models.ForeignKey(Perfil, related_name="puntuacioUsuari")
    
    class Meta:
        app_label = 'socials'

