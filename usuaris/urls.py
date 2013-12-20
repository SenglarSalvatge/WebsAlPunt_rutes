from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',

    url(r'^$', views.mostrarPerfil, name='mostrarPerfil') ,
    url(r'login', views.login, name='login')

)

