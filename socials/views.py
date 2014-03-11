from django.shortcuts import render
from socials.forms import ComentariForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from socials.models import Comentari

# Create your views here.
def entrarComentaris(request,id = None):
    if id is None:
        comentari = Comentari() 
        
    if request.method == 'POST':
        form = ComentariForm(request.POST, instance = comentari)
        if form.is_valid():
            messages.success(request, 'Form valid')
            form.save()
            #Mensajes bonitos, descomentar y borrar siguiente
            #messages.add_message(request, messages.SUCCESS, "Comentari Entrar Correctament")
            messages.success(request, 'Comentari entrat correctament')
        else:
            messages.error(request, 'Error')            
    else:
        form = ComentariForm(instance = comentari)

    return render(request, 'socials/entrarComentaris.html', {'form':form})

def llistarComentaris(request):
    return render(request, 'socials/llistarComentaris.html')