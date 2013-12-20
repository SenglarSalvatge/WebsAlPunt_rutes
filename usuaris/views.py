# -*- coding: utf-8 -*-
from django.shortcuts import render

def mostrarPerfil(request):
    return render(request, 'mostrarPerfil.html')

def login(request):
    #todo: fer render de login_social.html
    return render(request, 'login_social.html', {})
