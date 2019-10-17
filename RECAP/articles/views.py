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
    # article = get_object_or_404(Article, pk=article_pk), 아래 try~except 4줄 구문으로 바꿔준다.
    # 만약에 Article.objects.get(pk=article_pk)가 없으면? try안에 에러가 날 법한 소스를 넣어서 확인
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist: # 에러가 발생하면 아래를 실행
        raise Http404('해당하는 id의 글이 존재하지 않습니다.')
    
    c_form = CommentForm()
    # 위의 try 구문이 무리 없이 통과되면 아래 코드가 실행될 것
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

        # 전송된 데이터가 유효한 값인지 검사
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(
            #     title=title,
            #     content=content,
            #     )
            article = form.save() # 위에 여러 줄에 한 줄로 바뀌었다.
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
    # 2개 페이지 필요. 수정한 내용 보기/ 수정할 페이지 만들기 두 개의 함수를 method 기준으로 하나로 만들기
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        # 실제 DB의 데이터를 수정
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            form.save() # ArticleForm에 인자를 하나 더 넣어주면(instance=article), update로 동작
            return redirect(article)
    # 편집 화면
    form = ArticleForm(instance=article) # instance를 알아서 읽어오렴
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
        # 삭제는 GET보다 POST로
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
            # embed()
            # comment.article_id = article_pk
            # # 실제 DB에 반영이 되는 아래 실행문
            # comment.save()
            comment.article = article
            comment.save()
    # return redirect('articles:detail', article_pk)
    return redirect(article)


    # Comment.objects.create(
    #     content=request.GET.get('content'),
    #     article=Article.objects.get(pk=article_pk),
    # )
    # return redirect('articles:detail',article_pk)


def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        if comment.article == article:
            comment.delete()
    return redirect(article)