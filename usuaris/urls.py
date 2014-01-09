from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
    
    #mostrem el perfil d'usuari: /usuaris/perfil
    url(r'^usuaris/perfil/$', views.mostrarPerfil, name='mostrarPerfil'),
    
    #mostrem l'autenticacio per social auth: /usuaris/autenticacio
    url(r'^usuaris/autenticacio/$', views.login, name='login')

)

