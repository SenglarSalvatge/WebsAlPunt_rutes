# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    #foto //encara en fase de desenvolupament
    descripcio = models.CharField(max_length=800, help_text="Descripció")
    puntuacio = models.IntegerField(help_text="Puntuació")
    
    usuari = models.OneToOneField(User, help_text="Usuari")
    
    def __unicode__(self):  
        return self.id
