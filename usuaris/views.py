# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout
from models import Perfil
from django.shortcuts import get_object_or_404

def mostrarPerfil(request):
    return render(request, 'mostrarPerfil.html')

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
