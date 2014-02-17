# -*- coding: utf-8 -*-
import urllib2
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post
from posts.forms import PostForm, FiltreRutaForm
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import math

def mostrarRutes(request):
    Rutes = Post.objects.all()
    return render(request, 'posts/mostrarRutes.html', {'Rutes':Rutes})

def calcularDistanciaMapa(frase):
            listCoordenades = list()  
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
            while i < len(listCoordenades)-3:
                x1 = float(listCoordenades[i])
                i=i+1
                y1 = float(listCoordenades[i])
                i=i+1
                x2 = float(listCoordenades[i])
                i=i+1
                y2 = float(listCoordenades[i])
                i=i-1
                resultado =math.sqrt((x2-x1)**2+(y2-y1)**2)
                distancia= distancia +resultado
            
            return distancia
        
def calcularDuradaMapa(modo, distancia):     
            tiempo = 0
            if modo == "Caminada": 
                tiempo = distancia/5
            elif modo == "Bicicleta":
                tiempo = distancia/25
            elif modo == "Fotting": 
                tiempo = distancia/10
            elif modo == "Cavall": 
                tiempo = distancia/7
            
            return tiempo


def eliminarRuta(request, ruta_id):
    ruta=get_object_or_404(Post, pk=ruta_id)
    ruta.delete()
    
    url_next= reverse('posts:mostrarRutes', kwargs={})
    return HttpResponseRedirect(url_next)

def apuntarRuta(request, ruta_id):
    ruta=get_object_or_404(Post, pk=ruta_id)
    ruta.apuntats = request.user.perfil
    ruta.save()
    messages.info(request, 'Apuntat. ')
        
    url_next= reverse('posts:mostrarRutes', kwargs={})
    return HttpResponseRedirect(url_next)


def editaRuta(request, ruta_id=None):

    if ruta_id is not None:
        ruta=get_object_or_404(Post, pk=ruta_id)
    else:
        ruta=Post()
        
    if request.method == 'POST':
        form=PostForm(request.POST, instance=ruta)
       
        if form.is_valid():
            # solucion correcta:
            r = form.save(commit=False)
            #agafa coordenades
            frase = r.coordenades
            distancia = calcularDistanciaMapa(frase);
            # calcular tiempo 
            modo = r.categoria
            tiempo = calcularDuradaMapa(modo, distancia)
            #save
            r.km= distancia
            r.administrador=request.user.perfil
            #r.apuntats= r.administrador
            r.durada = tiempo
            r.save()
    
            messages.info(request, 'Ruta guardada. ')
            url_next= reverse('index', kwargs={})
            return HttpResponseRedirect(url_next)
        else:
            messages.error(request, 'petada general')
    else:
        form=PostForm(instance=ruta)
    
    return render(request, 'posts/novaRuta.html', {
        'form':form,
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
