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
    # desapuntar-se ruta
    url(r'^desapuntarRuta/(?P<ruta_id>\d+)/$', views.desapuntarRuta, name='desapuntarRuta'),
    # buscar ruta
    url(r'^buscarRuta/$', views.filtreDeRutes, name='buscarRuta'),
    # detall ruta
    url(r'^detall/(?P<ruta_id>\d+)/$', views.detall_ruta, name='detall'),
    # puntuar ruta
    url(r'^puntuar$', views.puntuar, name='puntuar'),
    # ruta acabada
    url(r'^rutaAcabada/$', views.mostrarRutesAcabades, name='mostrarRutesAcabades'),

)
