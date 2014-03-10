# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from posts.models import Post
from posts.forms import PostForm, FiltreRutaForm
from django.http.response import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import math
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.utils.datetime_safe import datetime, date
from socials.models import Puntuacio


def mostrarRutes(request):
    q_admin = Q( administrador = request.user.perfil )
    q_apuntat = Q( apuntats = request.user.perfil ) 
    Rutes = Post.objects.filter( q_admin | q_apuntat )
    return render(request, 'posts/mostrarRutes.html', {'Rutes':Rutes})

def mostrarRutesAcabades(request):    
    dataRuta = date.today()
    Rutes = Post.objects.filter(data__lt = dataRuta)    
    return render(request, 'posts/mostrarRutesAcabades.html', {'Rutes':Rutes})

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
            i = 0
            distancia = 0
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

#@permission_required('polls.can_vote', login_url='/loginpage/')
@login_required
def eliminarRuta(request, ruta_id):
    ruta=get_object_or_404(Post, pk=ruta_id)
    
    #seguretat:
    if ruta.administrador != request.user.perfil:
        return Http404
    
    ruta.delete()
    
    url_next= reverse('posts:mostrarRutes', kwargs={})
    return HttpResponseRedirect(url_next)

def apuntarRuta(request, ruta_id):
    ruta = get_object_or_404(Post, pk=ruta_id)
    
    p = request.user.perfil
    ruta.apuntats.add( p )
    ruta.save()
    
    messages.info(request, 'T\'has apuntat correctament a aquesta ruta. ')
        
    url_next= reverse('posts:mostrarRutes', kwargs={})
    return HttpResponseRedirect(url_next)

def desapuntarRuta(request, ruta_id):
    ruta = get_object_or_404(Post, pk=ruta_id)
    
    p = request.user.perfil
    ruta.apuntats.delete( p )
    ruta.save()
    
    messages.add_message(request, messages.ERROR, "T\'has desapuntat d'aquesta ruta. ")
    
    url_next = reverse('post:mostrarRutes', kwargs={})
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
            messages.add_message(request, messages.SUCCESS, "Ruta creada correctament")
            #messages.info(request, 'Ruta guardada. ')
            url_next= reverse('index', kwargs={})
            return HttpResponseRedirect(url_next)
        else:
            #messages.ad
            messages.error(request, 'petada general')
    else:
        form=PostForm(instance=ruta)
    
    return render(request, 'posts/novaRuta.html', {
        'form':form,
        })

def detall_ruta(request, ruta_id):
    ruta = Post.objects.filter(pk = ruta_id)
    return render(request, 'posts/detall.html', {'ruta':ruta})

def filtreDeRutes(request):

    form = FiltreRutaForm()
    if request.method == 'POST':
        #prepareu diccionari amb els parametres del post
        form = FiltreRutaForm(request.POST)        
        if form.is_valid():
            q_str = request.POST.copy()
            q_str.pop('csrfmiddlewaretoken') #borrem el srtdgf de l'array
            q = json.dumps(q_str)

            url_next = reverse('posts:buscarRuta', kwargs={})
        
            return HttpResponseRedirect(url_next+"?q="+q)
    
    else:
        q_str = request.GET.get('q',None)        
        
        if q_str:
            q = json.loads(q_str)        
            p = Q()
            
            print q
            
            #['titol', 'data', 'dificultat', 'categoria', 'administrador']
            if 'titol' in q and q['titol']:
                p &= Q(titol = q['titol'])
            if 'data' in q and q['data']:
                d = datetime.strptime(q['data'], '%d/%m/%Y')
                p &= Q(data = d)
            if 'dificultat' in q and q['dificultat']:
                p &= Q(dificultat = q['dificultat'])

            if 'categoria' in q and q['categoria']:
                n = int(q['categoria'])
                p &= Q(categoria = n)
            if 'administrador' in q and q['administrador']:
                n = int(q['administrador'])
                p &= Q(administrador = n)
            
            llista_rutes = Post.objects.filter( p )

        else:
            llista_rutes = Post.objects.none()
            
        page = request.GET.get('page')
        rutes = paginaitor_plus(page, llista_rutes, 2)
        
    return render(request, 'posts/filtreDeRutes.html', {'form':form, 'rutes':rutes, 'q':q_str})


def puntuar(request):
    punts = request.GET.get('punts')
    ruta_id = request.GET.get('ruta_id')
    ruta = get_object_or_404(Post, id = ruta_id )
    usuari = request.user.perfil
    
    p, created = Puntuacio.objects.get_or_create( post = ruta, perfil = usuari , defaults={'puntuacio':punts})
    p.puntuacio = punts
    p.save() 
    
    resposta = dict()
    resposta['resultat'] = 'OK'
    resposta['mitjana'] = ruta.mitjana
    resposta['punts'] = p.puntuacio
    
    return HttpResponse(json.dumps(resposta), content_type='application/json')


def paginaitor_plus(page, llista, num):
    paginator = Paginator(llista, num) #numero d'entrades per pàgina
    try:
        entrada = paginator.page(page)
    except PageNotAnInteger:
        entrada = paginator.page(1)
    except EmptyPage:
        entrada = paginator.page(paginator.num_pages)
    return entrada

