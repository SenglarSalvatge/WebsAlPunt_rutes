# -*- coding: utf-8 -*-
from django.shortcuts import render
import urllib
import urllib2
from django.utils.encoding import smart_str
from django.http.response import HttpResponse


def mostrarRutes(request):
    return render(request, 'posts/mostrarRutes.html')

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
