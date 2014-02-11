from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^ruta/$', views.mostrarRutes, name='mostrarRutes'),
    # crear ruta
    url(r'^novaRuta/$', views.editaRuta, name='novaRuta'),
    # edita ruta
    url(r'^editaRuta/(?P<ruta_id>\d+)/$', views.editaRuta, name='editaRuta'),
    # buscar ruta
    url(r'^buscarRuta/$', views.filtreDeRutes, name='buscarRuta'),

)
