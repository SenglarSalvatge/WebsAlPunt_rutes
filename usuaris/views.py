# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout
from models import Perfil
from django.http.response import HttpResponseRedirect
from usuaris.forms import PerfilForm
from django.contrib import messages
from django.core.urlresolvers import reverse

def editarPerfil(request):
    perfil = request.user.perfil
        
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance = perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil entrat correctament')
            url_next = reverse('usuaris:mostrarPerfil')            
            return HttpResponseRedirect( url_next )
        else:
            messages.error(request, 'Error')            
    else:
        form = PerfilForm(instance = perfil)

    return render(request, 'usuaris/editarPerfil.html', {'form':form})

def mostrarPerfil(request):
    return render(request, 'usuaris/mostrarPerfil.html')

def login(request):
    #todo: fer render de login_social.html
    return render(request, 'usuaris/login_social.html', {})

def exit_login(request):
    logout(request)
    return render(request, 'index.html', {})

def loginUsuari(request):
    variable = request.GET.get('access_token')
    if variable is not None:
        p = Perfil.objects.filter(token=variable)
    else:
        p = Perfil()
        p.nick = "AleX"
        p.token = variable
        p.save()
    return render(request, 'usuaris/mostrarRequest.html')