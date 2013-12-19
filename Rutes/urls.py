from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #arrel de la web: /
    url(r'^$', 'Rutes.views.index', name='index'),
    
    #url(r'^usuaris/', include('usuaris.urls')),
    
    #directori d'administració: /admin
    url(r'^admin/', include(admin.site.urls)),
)