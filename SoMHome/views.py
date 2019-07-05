from django.shortcuts import render
from . models import Post

def home(request):
    context = {}
    return render(request, 'SoMHome/home.html', context)

def about(request):
    context = {'title':'About'}
    return render(request, 'SoMHome/about.html', context)

def blog(request):
    context = {'title':'Blog', 'posts': Post.objects.all()}
    return render(request, 'SoMHome/blog.html', context)
