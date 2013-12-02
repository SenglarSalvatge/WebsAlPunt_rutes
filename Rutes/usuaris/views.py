#-*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"Benvingut a la pàgina principal de Activi.cat.")