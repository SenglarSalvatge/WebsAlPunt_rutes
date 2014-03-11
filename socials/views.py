from django.shortcuts import render
from socials.forms import ComentariForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from socials.models import Comentari
from posts.models import Post

# Create your views here.
def entrarComentaris(request,id_ruta,id_comentari = None):
    if id_comentari is None:
        comentari = Comentari()
    else:
        comentari = Comentari.objects.get(pk = id_comentari) 
     
    if request.method == 'POST':
        form = ComentariForm(request.POST, instance = comentari)
        if form.is_valid():
            s = form.save(commit = False)
            user_perfil = request.user.perfil
            user_ruta = Post.objects.get(pk = id_ruta)
            s.perfil = user_perfil
            s.post = user_ruta
            s.save()
            messages.success(request, 'Comentari entrat correctament')
        else:
            messages.error(request, 'Error')            
    else: 
        form = ComentariForm(instance = comentari)

    return render(request, 'socials/entrarComentaris.html', {'form':form, 'ruta':id_ruta})

def llistarComentaris(request):
    return render(request, 'socials/llistarComentaris.html')