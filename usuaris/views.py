#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(u"Benvingut a la pàgina principal de Activi.cat")

def login(request):
    #todo: fer render de login_social.html
    return render(request, 'login_social.html', {})