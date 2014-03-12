# -*- encoding: utf-8 -*-
from django.db import models
from usuaris.models import Perfil
from socials.models import Puntuacio, Comentari

class Categoria(models.Model):
    nom = models.CharField(max_length=200, help_text="Nom de la Categoria")
    foto = models.ImageField(upload_to='categoria_img', verbose_name='imatge', blank=True)
    
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
    dificultat = models.CharField(max_length=2, null=True, choices=DIFICULTAT_CHOICES, help_text="Dificultat")
        
    categoria = models.ForeignKey(Categoria, help_text="Categoria")
    administrador = models.ForeignKey(Perfil, help_text="Administrador", related_name="postAdministrats")
    apuntats = models.ManyToManyField(Perfil, blank = True, help_text="Apuntats", related_name="postOnEsticApuntat")
    coordenades = models.CharField(max_length=50000, help_text="Coordenades de la linea que marca la ruta", null=True)
    km = models.CharField(max_length=100, help_text="Kilometres de distancia")
    durada = models.CharField(max_length=50000, help_text="Durada de la ruta")
    
    puntuacions = models.ManyToManyField(Perfil, through='socials.Puntuacio', related_name="puntuacioPost")
    comentaris = models.ManyToManyField(Perfil, through='socials.Comentari', related_name="comentariPost")
    
    def __unicode__(self):  
        return self.titol
    
    @property
    def mitjana(self):
        from django.db.models import Avg
        calcula = Puntuacio.objects.filter( post= self).aggregate(mitjana = Avg('puntuacio'))
        return calcula['mitjana']
    
    def contador_comentaris(self):
        from django.db.models import Sum
        calcula = Comentari.objects.filter( pk = self).aggregate( suma = Sum('comentari'))
        return calcula['suma']
    
    def contador_participants(self):
        from django.db.models import Sum
        calcula = Post.objects.filter( pk = self).aggregate( suma = Sum('apuntats'))
        return calcula['suma']
    
    



