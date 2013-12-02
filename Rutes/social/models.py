# -*- encoding: utf-8 -*-
from django.db import models
from rutes.models import Post
from usuaris.models import Perfil

class Comentari(models.Model):
    comentari = models.CharField(max_length=800, help_text="Comentari")
    post = models.ForeignKey(Post)
    perfil = models.ForeignKey(Perfil,  related_name="comentariUsuari")
    
    class Meta:
        app_label = 'social'

class Puntuacio(models.Model):
    
    PUNTUACIO_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    
    puntuacio = models.CharField(max_length=1, choices=PUNTUACIO_CHOICES, help_text="Puntuació")
    post = models.ForeignKey(Post)
    perfil = models.ForeignKey(Perfil, related_name="puntuacioUsuari")
    
    class Meta:
        app_label = 'social'
