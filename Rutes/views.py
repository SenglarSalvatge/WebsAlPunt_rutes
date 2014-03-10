# -*- coding: utf-8 -*-
from django.shortcuts import render
from posts.models import Post

def index(request):
    rutes = Post.objects.all().order_by('-data')[:5] #últimes 10 rutes públicades
    return render(request, 'index.html', {'rutes':rutes,})    