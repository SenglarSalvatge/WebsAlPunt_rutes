from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',

    url(r'^perfil/$', views.mostrarPerfil, name='mostrarPerfil') ,
    url(r'^autenticacio/$', views.login, name='login')

)

