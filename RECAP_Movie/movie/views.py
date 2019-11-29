from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import Http404, HttpResponse, JsonResponse
from .forms import MovieForm, ReviewForm
from .models import Movie, Review
from IPython import embed
from itertools import chain

# Create your views here.
@login_required
def index(request):
    visits_num = request.session.get('visits', 0)
    request.session['visits'] = visits_num + 1
    request.session.modified = True
    followings_movies = request.user.followings.all()
    followings_and_me = chain(followings_movies, [request.user])
    total_movies = Movie.objects.filter(user__in=followings_and_me)
    
    context = {
        'movies': total_movies,
        'visits': visits_num,
    }
    return render(request, 'movie/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movies = movie_form.save(commit=False)
            movies.user = request.user
            movies.save()
            return redirect(movies)
        else:
            return redirect('movies:create')
    else:
        context = {
            'movie_form': MovieForm(),
        }
    return render(request, 'movie/create.html', context)


def detail(request, movie_pk):
    try:
        movies = Movie.objects.get(pk=movie_pk)
    except Movie.DoesNotExist:
        raise Http404('해당하는 id의 글이 존재하지 않습니다.')
    review_form = ReviewForm()
    context = {
        'movies': movies,
        'reviews': movies.review_set.all(),
        'review_form': review_form,
        'reviews1': Review.objects.all()
    }
    return render(request, 'movie/detail.html', context)

@login_required
@require_POST
def delete(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.user == request.user:
            if request.method == "POST":
                movie.delete()
                return redirect('movies:index')
            else:
                return redirect(movie)
    return HttpResponse('검증되지 않은 유저 정보입니다.', status=401)

@login_required
def update(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    if movies.user == request.user:
        if request.method == "POST":
            movie_form = MovieForm(request.POST, instance=movies)
            if movie_form.is_valid():
                movie_form.save()
                return redirect(movies)
        movie_form = MovieForm(instance=movies)
    else:
        return redirect('movies:index')
    context = {
        'movies': movies,
        'movie_form': movie_form,
    }
    return render(request, 'movie/update.html', context)

@login_required
def create_review(request, movie_pk):
    movies = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = movies
            review.user = request.user
            review.save()
    return redirect(movies)


def send_cookie(reqeust):
    # return render() -> html 페이지를 만들어주는 것(지금까지 한 것1)
    # return redirect() -> render를 해주는 url로 던져주는 것(지금까지 한 것2)
    # return reverse() -> 절대경로 지정할 때 썼던 것
    # return HttpResponse() -> HttpResponse 객체를 날려주기도 했었음
    
    res = HttpResponse('과자 받아라') # res 변수에 HttpResponse 클래스 객체를 생성해보자
    res.set_cookie('mycookie', 'Oreo') # python dictionary의 key:value 느낌으로 쿠키가 만들어짐
    return res

@require_POST
def like(request, movie_pk):
    # movie_pk 로 넘어온 글의 like_users에 현재 접속 중인 user를 추가한다.
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    # 만약 좋아요 리스트에 현재 접속중인 유저가 있다면,
    # 해당 유저는 좋아요를 했다.
    # if request.user in movie.like_users.all(): 비효율적인 방법
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user) # 좋아요 취소
        liked = False
    # 그렇지 않으면
    # 해당 유저는 아직 좋아요를 하지 않았다
    else:
        movie.like_users.add(user) # 좋아요 
        liked = True

    context = {
        'liked': liked,
        'count': movie.like_users.count(),
        'likeusers': list(movie.like_users.all().values_list('username', flat=True)),
    }

    return JsonResponse(context) # JsonResponse의 인자로는 딕셔너리가 온다. Python 딕셔너리를 Json으로 바꿔주는 함수

def dislike(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.like_users.remove(request.user)
    return redirect(movie)