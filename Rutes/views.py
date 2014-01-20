# -*- coding: utf-8 -*-
from django.shortcuts import render
from posts.models import Post

def index(request):
    rutes = Post.objects.all()   
    return render(request, 'index.html', {'rutes':rutes})    