# -*- coding: utf-8 -*-
import urllib
import urllib2
from django.utils.encoding import smart_str
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.forms import PostForm, FiltreRutaForm
from posts.models import Post
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



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

@login_required(login_url='usuaris:login') 
def filtreDeRutes(request):
    rutes = "No hi ha resultats..."
    
    if request.method == 'POST': 
        form = FiltreRutaForm(request.POST) 

        if form.is_valid():
            
            rutes = Post.objects.all();
            #'titol', 'data', 'dificultat', 'categoria', 'administrador', 'puntuacions']
            if form.cleaned_data['titol']:
                rutes = rutes.objects.filter(titol = form.cleaned_data['titol'])
                
            if form.cleaned_data['data']:
                rutes = rutes.objects.filter(titol = form.cleaned_data['data'])
                
            if form.cleaned_data['dificultat']:
                rutes = rutes.objects.filter(titol = form.cleaned_data['dificultat'])
                
            if form.cleaned_data['categoria']:
                rutes = rutes.objects.filter(titol = form.cleaned_data['categoria'])
                
            if form.cleaned_data['administrador']:
                rutes = rutes.objects.filter(titol = form.cleaned_data['administrador'])
                
            if form.cleaned_data['puntuacions']:
                rutes = rutes.objects.filter(titol = form.cleaned_data['puntuacions'])
         
        
        return render(request, 'posts/filtreDeRutes.html', {'form':form, 'rutes':rutes})
        
    else:
        form = FiltreRutaForm()
    return render(request, 'posts/filtreDeRutes.html', {'form':form})
