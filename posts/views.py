# -*- coding: utf-8 -*-
from django.shortcuts import render


def mostrarRutes(request):
    return render(request, 'mostrarRutes.html')

def google(request):
    return render(request, 'provesgooglemaps.html')

#def googleResultats(request):
 #   request_data = urlllib.urlencode()
  #  response = urlilib2.urlopen("https://url of the virtual bank POS", request_data)
    
   # response_data = response.read()
    #data = response_data.split('\n')
    
    
    
    
    
