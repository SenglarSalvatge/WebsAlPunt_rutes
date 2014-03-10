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
    # buscar ruta
    url(r'^buscarRuta/$', views.filtreDeRutes, name='buscarRuta'),
    # detall ruta
    url(r'^detall/(?P<ruta_id>\d+)/$', views.detall_ruta, name='detall'),
    # puntuar ruta
    url(r'^puntuar$', views.puntuar, name='puntuar'),

)
