# -*- coding: utf-8 -*-
from django.shortcuts import render

def mostrarPerfil(request):
    return render(request, 'mostrarPerfil.html')
