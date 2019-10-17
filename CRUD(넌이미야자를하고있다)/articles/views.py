from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.

def index(request):
    articles = Articles.objects.all()

    context = {
        'articles': reversed(articles),
    }

    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')



def create(request):
    title = request.GET.get('title')
    contents = request.GET.get('contents')
    img_url = request.GET.get('img_url')

    article = Articles()
    article.title = title
    article.contents = contents
    article.img_url = img_url
    article.save()
    
    return redirect('index')
