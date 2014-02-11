from django.conf.urls import patterns, url
from socials import views

urlpatterns = patterns('',
    url(r'^comentari/$', views.entrarComentaris, name='entrarComentaris'),
    url(r'^llistat_comentari', views.llistarComentaris, name='llistarComentaris'),
)