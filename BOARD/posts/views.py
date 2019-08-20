from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    # table 형태로 게시판을 보여줌
    posts = Post.objects.all()

    context = {
        # DB에 있는 모든 데이터 들고 와
        'posts': reversed(posts)
    }
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    # new에서 날아온 데이터로 DB에 저장한다.
    # post = Post(
    #     title = request.GET.get('title'),
    #     content = request.GET.get('content'),
    #     image_url = request.GET.get('image_url'),
    # )
    # post.save()

    # Post.objects.create() 이런 것도 있으니 써보자. save를 대신할 수 있음.
    Post.objects.create(
        title = request.GET.get('title'),
        content = request.GET.get('content'),
        image_url = request.GET.get('image_url'),
    )

    # DB에 들어간 Column명과 input에 붙인 데이터의 이름이 같을 때 아래처럼 쓸 수 있음
    # 불순물 데이터가 있을 수도 있으니까 선택적으로 데이터를 사용하기 위해서는 이 방법 보다는 위에 있는 방법을 쓴다. 
    # Post.objects.create(**request.GET)
    # print(request.GET)
    return redirect('home')

def detail(request,pk):
    # pk라는 id를 가진 글을 찾아와 보여준다.
    # primary key
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)

def delete(request,pk):
    # pk라는 id를 가진 글을 삭제한다.
    # 일단 삭제할 글의 id를 찾는다.
    post = Post.objects.get(pk=pk)
    # 삭제하자!
    post.delete()

    return redirect('home')

def edit(request,pk):
    '''
    # pk라는 id를 가진 글을 편집하게 하기 위해서
    1. pk라는 id를 가진 글을 찾음
    2. 
    '''
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }

    return render(request, 'posts/edit.html', context)

def update(request, pk):
    '''
    1. pk라는 id를 가진 글을 찾아서,
    2. /edit/으로부터 날아온 데이터를 적용하여 변경한다.
    '''
    post = Post.objects.get(pk=pk)
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.image_url = request.GET.get('image_url')
    post.save()

    return redirect('posts:detail',pk)