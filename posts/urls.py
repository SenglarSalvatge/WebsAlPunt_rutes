from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^ruta/$', views.mostrarRutes, name='mostrarRutes'),
    # crear ruta
    url(r'^novaRuta/$', views.editaRuta, name='novaRuta'),
    # edita ruta
    url(r'^editaRuta/(?P<ruta_id>\d+)/$', views.editaRuta, name='editaRuta'),
    # eliminar ruta
    url(r'^eliminarRuta/(?P<ruta_id>\d+)/$', views.eliminarRuta, name='eliminarRuta'),
    # apuntar-se ruta
    url(r'^apuntarRuta/(?P<ruta_id>\d+)/$', views.apuntarRuta, name='apuntarRuta'),
    # desapuntar-se ruta
    url(r'^desapuntarRuta/(?P<ruta_id>\d+)/$', views.desapuntarRuta, name='desapuntarRuta'),
    # buscar ruta
    url(r'^buscarRuta/$', views.filtreDeRutes, name='buscarRuta'),
    # ruta acabada
    url(r'^rutaAcabada/$', views.mostrarRutesAcabades, name='mostrarRutesAcabades'),
)
