from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Hashtag
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from itertools import chain


# Create your views here.
@login_required
def index(request):
    visits_num = request.session.get('visits', 0)
    request.session['visits'] = visits_num + 1
    request.session.modified = True
    followings = request.user.followings.all()
    followings_and_me = chain(followings, [request.user])
    articles = Article.objects.filter(user__in=followings_and_me)
    # my_articles = request.user.article_set.all()
    context = {
        'articles': articles,
        'visits': visits_num
    }
    return render(request, 'articles/index.html', context)

# detail
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 만약에 Article.objects.get(pk=article_pk)
    # try:
    #     article = Article.objects.get(pk=article_pk)
    # except Article.DoesNotExist:
    #     raise Http404('해당하는 id의 글이 존재하지 않습니다.')
    comment_form = CommentForm()
    
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': article.comment_set.all(),
    }
    return render(request, 'articles/detail.html', context)
    

@login_required
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        
        form = ArticleForm(request.POST)
        # 전송된 데이터가 유효한 값인지 검사
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            # hashtag
            for word in article.content.split():
                if word.startswith('#'):
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)
            return redirect(article)
        else:
            return redirect('articles:create')
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)


# UPDATE -> articles/:id/update | (PUT) articles/:id
@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if article.user == request.user:
        if request.method == 'POST':
            # 실제 DB의 데이터를 수정
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect(article)
        
        # 편집 화면
        form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# DELETE -> articles/:id/delete
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.user == request.user:
            if request.method == 'POST':
                article.delete()
                return redirect('articles:index')
        else:
            return redirect(article)
    return HttpResponse('검증되지 않은 유저정보', status=401)

@login_required
def create_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # comment.article_id = article_pk
            # comment.save()
            comment.user = request.user
            comment.article = article
            comment.save()
    
    # return redirect('articles:detail', article_pk)
    return redirect(article)

def send_cookie(request):
    # return render() -> html 페이지를 만들어 주는 것.
    # return redirect()
    # return reverse()
    # return HttpResponse()
    res = HttpResponse('과자 받아라')
    res.set_cookie('mycookie', 'oreo')
    return res

def like(request, article_pk):
    # article_pk로 넘어온 글의 like_users에 현재 접속중인 유저를 추가한다.
    article = Article.objects.get(pk=article_pk)
    user = request.user
    # 만약 좋아요 리스트에 현재 접속중인 유저가 있다면,
    # -> 해당 유저는 좋아요를 했다
    # if request.user in article.like_users.all():
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)

    return redirect(article)
    # request.user.like_articles.add(article)

def explore(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/explore.html', context)

def tags(request):
    tags = Hashtag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'articles/tags.html', context)

def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    articles = hashtag.article_set.all()
    context = {
        'hashtag': hashtag,
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)