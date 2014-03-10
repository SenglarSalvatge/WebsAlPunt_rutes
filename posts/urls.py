from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^ruta/$', views.mevaRuta, name='mostrarRutes'),
    # crear ruta
    url(r'^novaRuta/$', views.editaRuta, name='novaRuta'),
    # les meves rutes 
    url(r'^mevaRuta/$', views.mevaRuta, name='mevaRuta'),
    # rutes on participare
    url(r'^participaRuta/$', views.participaRuta, name='participaRuta'),
    # edita ruta
    url(r'^editaRuta/(?P<ruta_id>\d+)/$', views.editaRuta, name='editaRuta'),
    # eliminar ruta
    url(r'^eliminarRuta/(?P<ruta_id>\d+)/$', views.eliminarRuta, name='eliminarRuta'),
    # apuntar-se ruta
    url(r'^apuntarRuta/(?P<ruta_id>\d+)/$', views.apuntarRuta, name='apuntarRuta'),
    # buscar ruta
    url(r'^buscarRuta/$', views.filtreDeRutes, name='buscarRuta'),
    # ruta acabada
    url(r'^rutaAcabada/$', views.mostrarRutesAcabades, name='mostrarRutesAcabades'),
)
