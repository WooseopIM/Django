from django.shortcuts import render, redirect
from datetime import datetime
from .models import Article

blogs = []

# Create your views here.
# class Article:
#     def __init__(self, title, content, created_at):
#         self.title = title
#         self.content = content
#         self.created_at = created_at

#     def __str__(self):
#         return f'제목: {self.title}, 내용: {self.content}, 작성시간: {self.created_at}'




    # 지금까지 작성된 모든 글들을 보여줌
    # 대표 url, root로 만들어 줄거야
    # articles.views.index
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': reversed(articles),
    }
    return render(request, 'index.html', context)

def articles(request):
    return render(request, 'articles.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    # new에서 날아온 데이터를 보여줌
    title = request.GET.get('title')
    contents = request.GET.get('contents')
    img_url = request.GET.get('img_url')

    # now = datetime.now()

    # DB에 저장하기
    article = Article()
    article.title = title
    article.contents = contents
    article.img_url = img_url
    article.save()

    context = {
        'title': title,
        'contents': contents,
        'img_url': img_url,
        'created_at': article.created_at,
    }
    return redirect('index')



