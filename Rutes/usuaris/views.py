from django.http import HttpResponse

def index(request):
    return HttpResponse("Benvingut a la pàgina principal de Activi.cat.")