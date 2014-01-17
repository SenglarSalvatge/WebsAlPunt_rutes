# -*- encoding: utf-8 -*-
from django.db import models
from usuaris.models import Perfil

class Categoria(models.Model):
    nom = models.CharField(max_length=200, help_text="Nom de la Categoria")
    
    def __unicode__(self):  
        return self.nom

class Dades_Mapa(models.Model):
    descripcio = models.CharField(max_length=800, help_text="Camp en fase de desenvolupament")

class Post(models.Model):
    
    DIFICULTAT_CHOICES = (
        ('BA', 'Baix'),
        ('IN', 'Intermig'),
        ('AL', 'Alt'),
        ('EX', 'Extrem'),
    )
    
    titol = models.CharField(max_length=200, help_text="Títol")
    data = models.DateField(help_text="Data")
    descripcio = models.CharField(max_length=800, help_text="Descripció")
    dificultat = models.CharField(max_length=2, blank=True, choices=DIFICULTAT_CHOICES, help_text="Dificultat")
    
    categoria = models.ForeignKey(Categoria, help_text="Categoria")
    administrador = models.ForeignKey(Perfil, help_text="Administrador", related_name="postAdministrats")
    apuntats = models.ManyToManyField(Perfil, help_text="Apuntats", related_name="postOnEsticApuntat")
    #mapa = models.OneToOneField(Dades_Mapa, help_text="Mapa")
    
    puntuacions = models.ManyToManyField(Perfil, through='socials.Puntuacio', related_name="puntuacioPost")
    comentaris = models.ManyToManyField(Perfil, through='socials.Comentari', related_name="comentariPost")
    
    def __unicode__(self):  
        return self.titol
