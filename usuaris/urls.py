from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
    url(r'^/$', views.mostrarPerfil, name='mostrarPerfil')
)
