# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout

def mostrarPerfil(request):
    return render(request, 'mostrarPerfil.html')

def login(request):
    #todo: fer render de login_social.html
    return render(request, 'usuaris/login_social.html', {})

def exit_login(request):
    logout(request)
    return render(request, 'index.html', {})