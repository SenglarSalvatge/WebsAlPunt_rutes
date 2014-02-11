# -*- coding: utf-8 -*-
import urllib2
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post, Dades_Mapa
from posts.forms import PostForm, FiltreRutaForm, CoordenadesForm
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import math



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
        mapa=Dades_Mapa()
    if request.method == 'POST':
        form=PostForm(request.POST, instance=ruta)
        form2=CoordenadesForm(request.POST, instance=mapa)
        if form.is_valid() and form2.is_valid():
            #print "---<",form.cleaned_data['postCoordenades']
            # solucion correcta:
            m=form2.save(commit=False)
            r=form.save(commit=False)
            #agafa coordenades
            listCoordenades = list()
            frase=m.coordenades
            #frase="(20,12)(12,12)(2,4)(5,3)"
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
                resultado =math.sqrt((x2-x1)^2+(y2-y1)^2)
                distancia= distancia +resultado
                
            # calcular tiempo 
            modo = ruta.categoria
            tiempo = 0
            if modo == "andar": 
                tiempo = distancia/5
            elif modo == "bicicleta":
                tiempo = distancia/25
            elif modo == "correr": 
                tiempo = distancia/10
            elif modo == "caballo": 
                tiempo = distancia/7
                
            # guardar dades
            
            m.km=distancia
            m.durada = tiempo
            m.save()
            
            r.mapa=mapa
            r.save()
    
                
             
            messages.info(request, 'Ruta guardada. ')
            url_next= reverse('posts:mostrarRutes', kwargs={})
            return HttpResponseRedirect(url_next)
        else:
            messages.error(request, 'error en el formulari. ')
        
    else:
        form=PostForm(instance=ruta)
        form2=CoordenadesForm(instance=mapa)
    
    
    return render(request, 'posts/novaRuta.html', {
        'form':form, 'form2':form2,
        })

@login_required(login_url='usuaris:login') 
def filtreDeRutes(request):
    
    if request.method == 'POST': 
        form = FiltreRutaForm(request.POST) 

        if form.is_valid():
            q = Q()
            
            #['titol', 'data', 'dificultat', 'categoria', 'administrador']
            if form.cleaned_data['titol']:
                q &= Q(titol = form.cleaned_data['titol'])
                
            if form.cleaned_data['data']:
                q &= Q(data = form.cleaned_data['data'])
            
            if form.cleaned_data['dificultat'] != '':
                if form.cleaned_data['dificultat']:
                    q &= Q(dificultat = form.cleaned_data['dificultat'])
                
            if form.cleaned_data['categoria']:
                q &= Q(categoria = form.cleaned_data['categoria'])
                
            if form.cleaned_data['administrador']:
                q &= Q(administrador = form.cleaned_data['administrador'])
                
        
            rutes = Post.objects.filter( q )
        
        return render(request, 'posts/filtreDeRutes.html', {'form':form, 'rutes':rutes})
        
    else:
        form = FiltreRutaForm()
    return render(request, 'posts/filtreDeRutes.html', {'form':form})
