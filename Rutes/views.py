# -*- coding: utf-8 -*-
from django.shortcuts import render
from posts.models import Post

def index(request):
    rutes = Post.objects.all()
    for ruta in rutes:
        print(ruta.titol)
        
    return render(request, 'index.html')    