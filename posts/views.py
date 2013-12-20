# -*- coding: utf-8 -*-
from django.shortcuts import render

def mostrarRutes(request):
    return render(request, 'mostrarRutes.html')
