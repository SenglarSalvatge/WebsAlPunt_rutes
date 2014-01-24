from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^ruta/$', views.mostrarRutes, name='mostrarRutes'),
    
    #proves per a google maps: CLIENT
    url(r'^mapes/$', views.google, name='google'),
    
    #proves per a google maps: CLIENT
    url(r'^mapes/resultats/(?P<coordenades>\d+)$', views.googleResultats, name='googleResultats'),
)
