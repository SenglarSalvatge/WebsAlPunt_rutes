# -*- encoding: utf-8 -*-
from django.db import models
from usuaris.models import Perfil
from socials.models import Puntuacio

class Categoria(models.Model):
    nom = models.CharField(max_length=200, help_text="Nom de la Categoria")
    
    def __unicode__(self):  
        return self.nom


class Post(models.Model):
    
    DIFICULTAT_CHOICES = (
        ('BA', 'Baix'),
        ('IN', 'Intermig'),
        ('AL', 'Alt'),
        ('EX', 'Extrem'),
    )
    
    titol = models.CharField(max_length=200, help_text="Títol")
    data = models.DateField(help_text="Data")
    descripcio = models.CharField(max_length=800, blank=True, null=True, help_text="Descripció")
    dificultat = models.CharField(max_length=2, blank=True, choices=DIFICULTAT_CHOICES, help_text="Dificultat")
    
    categoria = models.ForeignKey(Categoria, help_text="Categoria")
    administrador = models.ForeignKey(Perfil, help_text="Administrador", related_name="postAdministrats")
    apuntats = models.ManyToManyField(Perfil, blank = True, help_text="Apuntats", related_name="postOnEsticApuntat")
    coordenades = models.CharField(max_length=50000, help_text="Coordenades de la linea que marca la ruta")
    km = models.CharField(max_length=100, help_text="Kilometres de distancia")
    durada = models.CharField(max_length=50000, help_text="Durada de la ruta")
    
    puntuacions = models.ForeignKey(Puntuacio, blank = True, help_text="Puntuacions", null=True)
    comentaris = models.ManyToManyField(Perfil, through='socials.Comentari', related_name="comentariPost")
    
    def __unicode__(self):  
        return self.titol
