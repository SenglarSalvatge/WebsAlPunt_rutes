from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
   
    #mostrem el perfil d'usuari: /usuaris/perfil
    url(r'^perfil/$', views.mostrarPerfil, name='mostrarPerfil'),
    
    #mostrem l'autenticacio per social auth: /usuaris/autenticacio
    url(r'^autenticacio/$', views.login, name='login'),
    
    url(r'^loug_aut/$', views.exit_login, name='exit_login') ,
    
    url(r'^perfilUsuari/$', views.loginUsuari, name='iniciUsuari') ,
)
