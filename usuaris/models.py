# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from usuaris.utils_usuaris import inventat_un_nou_nick

class Perfil(models.Model):
    #foto //encara en fase de desenvolupament
    descripcio = models.CharField(max_length=800, blank=True)
    nick = models.CharField(max_length=50, blank=False)
    usuari = models.OneToOneField(User)
    
    def __unicode__(self):  
        return self.nick


#Antes de crear usuarios chupis
from django.db.models.signals import post_save

# definition of UserProfile from above
# ...

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #generar nick
        nick = inventat_un_nou_nick()
        Perfil.objects.create(usuari=instance, descripcio="", nick=nick )

# connectem event: després de que es crea l'usuari s'invoca la funció 'create_user_profile'
post_save.connect(create_user_profile, sender=User)