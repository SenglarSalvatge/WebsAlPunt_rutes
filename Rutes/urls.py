# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #arrel de la web: /
    url(r'^$', 'Rutes.views.index', name='index'),
    
    #mostrem l'apartat de rutes: /rutes/
    url(r'', include('posts.urls', namespace='posts')),
    
    #mostrem el perfil de l'usuari: /usuaris/
    url(r'', include('usuaris.urls', namespace='usuaris')),
    
    #directori d'administració: /admin/
    url(r'^admin/', include(admin.site.urls)),
    
    #auntenticacio de social auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    
    #proves per a google maps versio client
    url('', include('posts.urls', namespace='googlemaps')),
)