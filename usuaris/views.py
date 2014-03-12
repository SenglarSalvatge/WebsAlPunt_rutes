# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout
from models import Perfil
from socials.models import Comentari
from django.http.response import HttpResponseRedirect
from usuaris.forms import PerfilForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def editarPerfil(request):
    perfil = request.user.perfil
        
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance = perfil)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Perfil Modificat Correctament")
            url_next = reverse('usuaris:mostrarPerfil')            
            return HttpResponseRedirect( url_next )
        else:
            messages.add_message(request, messages.ERROR, "Error Modificant El Perfil")
            #messages.error(request, 'Error Modificant El Perfil')            
    else:
        form = PerfilForm(instance = perfil)

    return render(request, 'usuaris/editarPerfil.html', {'form':form})

def mostrarPerfil(request):
    comentaris = Comentari.objects.filter(perfil = request.user.perfil) 
    return render(request, 'usuaris/mostrarPerfil.html', {'comentaris':comentaris})


def eliminarComentari(request, comentari_id):
    coment=get_object_or_404(Comentari, pk=comentari_id)
    #seguretat
    if coment.perfil != request.user.perfil:
            url_next= reverse('index', kwargs={})
            return HttpResponseRedirect(url_next)
    coment.delete()
    url_next= reverse('usuaris:mostrarPerfil', kwargs={})
    return HttpResponseRedirect(url_next)

def login(request):
    #todo: fer render de login_social.html
    return render(request, 'usuaris/login_social.html', {'xrequest':request})

def exit_login(request):
    logout(request)
    return render(request, 'index.html', {})
