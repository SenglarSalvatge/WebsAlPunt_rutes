# -*- coding: utf-8 -*-
import urllib
import urllib2
from django.utils.encoding import smart_str
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.forms import PostForm
from posts.models import Post, Dades_Mapa
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
        mapa = get_object_or_404(Dades_Mapa, pk=ruta.mapa.pk )
    else:
        ruta=Post()
        mapa=Post()
    if request.method == 'POST':
        form=PostForm(request, instance=ruta)
        if form.is_valid():
            print "---<",form.cleaned_data['postCoordenades']
            # solucion correcta:
            
            #r=form.save(commit=False)
            #r.mapa=lala
            #r.save()

            #agafa coordenades
            listCoordenades = list()
            frase="(20,12)(12,12)(2,4)(5,3)"
            frase=frase[1:]
            frase=frase[:-1]
            arrayFrase=frase.split(")(")
            # omplo la list amb les coordenades
            for x in arrayFrase:
                frase2= x.split(",")
                coordenada1= frase2[0]
                coordenada2= frase2[1]
                #listCoordenades.append( (coordenada1,coordenada2) )
                listCoordenades.append(coordenada1)
                listCoordenades.append(coordenada2)
            # calculo la distancia    
            i =0
            distancia=0
            while i < len(listCoordenades):
                x1 = float(listCoordenades[i])
                i=i+1
                y1 = float(listCoordenades[i])
                i=i+1
                x2 = float(listCoordenades[i])
                i=i+1
                y2 = float(listCoordenades[i])
                i=i-1
                #resultado =SQR((x2-x1)^2+(y2-y1)^2
                #distancia= distancia +resultado
                
            # calcular tiempo 
            modo = "avion"
            tiempo = 0
            if modo == "andar": 
                tiempo = distancia/5
            elif modo == "bicicleta":
                tiempo = distancia/25
            elif modo == "correr": 
                tiempo = distancia/10
            elif modo == "caballo": 
                tiempo = distancia/7
             
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
