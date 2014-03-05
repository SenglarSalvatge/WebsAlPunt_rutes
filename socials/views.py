from django.shortcuts import render
from socials.forms import ComentariForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def entrarComentaris(request):
    if request.method == 'POST':
        form = ComentariForm(request.POST)
        if form.is_valid():
            form.save()
            #Mensajes bonitos, descomentar y borrar siguiente
            #messages.add_message(request, messages.SUCCESS, "Comentari Entrar Correctament")
            messages.success(request, 'Comentari entrat correctament')
            url_next = reverse('socials:entrarComentaris')            
            return HttpResponseRedirect( url_next )
        else:
            messages.error(request, 'Error')            
    else:
        form = ComentariForm()

    return render(request, 'socials/entrarComentaris.html', {'form':form})

def llistarComentaris(request):
    return render(request, 'socials/llistarComentaris.html')