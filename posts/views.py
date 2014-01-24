# -*- coding: utf-8 -*-
import urllib
import urllib2
from django.utils.encoding import smart_str
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.forms import PostForm
from posts.models import Post
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse



def google(request):
    return render(request, 'posts/provesgooglemaps.html')

def googleResultats(request, coordenades):
    #url valida
    #http://maps.googleapis.com/maps/api/directions/json?origin=*&destination=*&sensor=false
    url = 'http://maps.googleapis.com/maps/api/directions/json?'
    parametres = {'origin':'(40,3)',
                  'destination':'(40,2)',
                  'sensor':'false',
                  }
    url_final = url+parametres
    request = urllib2.Request(url_final)
    response = urllib2.urlopen(request)
    html = response.read()
    
    return HttpResponse(html)

def mostrarRutes(request):
    Rutes = Post.objects.all()
    return render(request, 'posts/mostrarRutes.html', {'Rutes':Rutes})


def editaRuta(request, ruta_id=None):

    if ruta_id is not None:
        ruta=get_object_or_404(Post, pk=ruta_id)
    else:
        ruta=Post()
    if request.method == 'POST':
        form=PostForm(request, instance=ruta)
        if form.is_valid():
     
            
            # solucion correcta:
            
            #r=form.save(commit=False)
            #r.mapa=lala
            #r.save()

            messages.info(request, 'Ruta guardada. ')
            url_next= reverse('posts:mostrarRutes', kwargs={})
            return HttpResponseRedirect(url_next)
        else:
            messages.error(request, 'error en el formulari. ')
        
    else:
        form=PostForm(instance=ruta)
        
    return render(request, 'posts/novaRuta.html', {
        'form':form,
        })
