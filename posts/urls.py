from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^rutes/$', views.mostrarRutes, name='mostrarRutes'),
    
    #proves per a google maps
    url(r'^mapes/$', views.google, name='google'),
    #url(r'^mapes/resultats/$', views.googleResultats, name='googleResultats'),
)
