from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Post
import requests
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': reversed(posts)
    }
    return render(request, 'posts/index.html', context)

def detail(request,pk):
    posts = Post.objects.get(pk=pk)
    context = {
        'posts': posts
    }
    return render(request, 'posts/detail.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('posts:index')
    else:
        return render(request, 'posts/create.html')

def update(request,pk):
    posts = Post.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        posts.title = title
        posts.content = content
        posts.save()
        return redirect('posts:detail',pk)
    else:
        context = {
            'posts': posts

        }

        return render(request, 'posts/update.html', context)

def delete(request,pk):
    posts = Post.objects.get(pk=pk)
    posts.delete()
    return redirect('posts:index')

