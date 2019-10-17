```
'''
urls.py
'''
from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/delete/', views.delete, name="delete"),
    path('<int:article_pk>/update', views.update, name="update"),
    path('<int:article_pk>/comments/', views.create_comment, name="create_comment"),
    path('<int:article_pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name="comment_delete"),
]


'''
views.py
'''

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.http import Http404
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# detail
def detail(request,article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist: # 에러가 발생하면 아래를 실행
        raise Http404('해당하는 id의 글이 존재하지 않습니다.')
    
    c_form = CommentForm()
    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'c_form': c_form,
    }
    return render(request, 'articles/detail.html', context)

# create
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            article = form.save()
            return redirect(article)
        else:
            return redirect('articles:create')
    else:
        context = {
            'form':ArticleForm(),
        }
        return render(request, 'articles/create.html', context)

# UPDATE: articles/id/update | PUT(articles/id)
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
        	form.save()
            return redirect(article)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

# DELETE: articles/id/delete | 
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)


def create_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()

    return redirect(article)


def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        if comment.article == article:
            comment.delete()
    return redirect(article)
    
    
'''
models.py
'''
from django.db import models
from django.urls import reverse

# Create your models here.
# 모델은 title, content, created_at, updated_at

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)

    # method도 추가예정
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': self.pk})


class Comment(models.Model):
    comment = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.comment

    # def get_absolute_url(self):
    #     return reverse('articles:detail', kwargs={'article_pk':self.article.pk})
    
    
    
'''
forms.py
'''from django import forms
from .models import Article, Comment

# class Article(models.Model)
# class ArticleForm(forms.Form):



# 현재 모델폼이 갖고 있는 정보를 Meta 클래스에 정의
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)

    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20자 이내로 써주세요.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-title',
                'placeholder': '제목을 입력해주세요.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '내용을 입력해주세요.',
                'rows': 5,
            }
        )
    )

        # exclude = ('title',) title에 대해서는 Form을 만들지 않는다.
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'placeholder': "제목을 입력해주셈",
        #         'class': 'form-control title-class',
        #         'id': 'title',
        #     })
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
    
    comment = forms.CharField(
        label='댓글',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control comments',
                'placeholder': '댓글을 입력해주세요',
                'rows': 2,
                'cols': 50,
            }
        ),
    )








<!-- base.html -->
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  {% block body %}
  {% endblock %}
</body>
</html>


<!-- index.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}
<div class="container">
  <h1 id='title'>여기에 내용물이 들어갈거야(Articles)</h1>
  <a class="btn btn-info" href="{% url 'articles:create' %}">새글쓰기</a>

  <!-- 모든 Articles들을 보여줌 -->
  {% for article in articles %}
  <p>{{ article.pk }}</p>
  <p>{{ article.title }}</p>
  <a href="{{ article.get_absolute_url }}">상세보기</a>
  {% endfor %}
</div>


{% endblock %}


<!-- create.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}
<div class="container">
  <h1>새글쓰기(input태그이용)</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit">
  </form>
</div>

{% endblock %}


<!-- detail.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}
<div class="container">
  <h1>상세보기</h1>
  <p>번호 : {{ article.pk }}</p>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>생성일자 : {{ article.created_at|date:"Y년, m월, d일" }}</p>
  <p>수정일자 : {{ article.updated_at|date:"SHORT_DATE_FORMAT" }}</p>
  <a href="{% url 'articles:index' %}" class="btn btn-success">목록보기</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제" class="btn btn-danger">
  </form>
  <a href="{% url 'articles:update' article.pk %}">수정</a>

  <hr>
  
  <h2>댓글 목록</h2>
  
  <form action="{% url 'articles:create_comment' article.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form c_form %}
    <input type="submit" class="btn btn-secondary">
  </form>
  <hr>
    <p><i>총 {{ comments | length }}개의 댓글이 달렸습니다.</i></p>
    {% for comment in comments %}
      <p>{{ comment.comment }}</p>
      <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method='POST'>
        {% csrf_token %}
        <input type="submit" value="댓삭" class="btn btn-danger">
      </form>
    {% empty %}
      <p><i>아직 댓글이 없어요. 댓글 달아주세요</i></p>
    {% endfor %}
</div>

{% endblock %}


<!-- update.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}
<div class="container">
  <h1>글 수정</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit">
  </form>
</div>

{% endblock %}
```

