# Project 06 (최종완성)

> 프레임워크 기반 웹 페이지 구현.
>
> - 파이썬 웹 프레임워크를 통한 데이터 조작
> - Object Relational Mapping에 대한 이해
> - Template Variable을 활용한 Template 제작
> - Static 파일 관리

---

## 준비사항

1. Python Web Framework - Django

2. Python Web Framework 사용을 위한 환경설정

   -가상환경 Python 3.7+

----

## 결과물 REVIEW

1. 부스트스랩 Stater Templates을 Copy & Paste 하는 방식이 아니라, Django와 파이썬에서 제공하는 {% load bootstrap4 %}를 활용하는 점이 신기했고 앞으로 자주 쓰게 될 것 같다.

2. 영화 목록 페이지 구현할 때 목록 상단에 영화와 관련한 이미지를 서버에 저장된 이미지로 활용하라는 명세가 있었는데, static 경로 설정을 의미하는 것 같았다. 오래전 배운 기억 + 구글링으로 간신히 했는데 잘 된건지 모르겠다.

   bash 창에서 아래 메시지가 뜸.
   
   
```bash
$ python manage.py collectstatic
```

```bash
$ python manage.py collectstatic
Found another file with the destination path 'movie-918655_1920.jpg'. It will be ignored since only the first encountered file is collected. If this is not what you want, make sure every static file has a unique path.
```
----

## 요구사항 구현

### 1. 데이터베이스

> 영화에 대한 정보를 명세에 나온대로 Django의 모델 클래스를 상속하여 Movie 클래스를 만들어준다.
>
> 개별 영화에 대한 한줄평을 생성해줄 수 있는 Review 클래스도 Django의 모델 클래스를 상속하여 만들어주는데, 주의할 점은 외래키를 지정해줘야 한다. 해당하는 글에 대해서만 한줄평을 작성해야하기 때문.

```python
from django.db import models
from django.urls import reverse
class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    audience = models.IntegerField()
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=30)
    watch_grade = models.TextField()
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    
    class Meta:
        ordering = ('-pk',)
    
    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'movie_pk': self.pk})
```

```python
class Review(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-pk',)
```

-  평점(score)은 정수가 아니므로 `FloatField()`를 적용시킨다.
- 개봉일(open_date)는 `DateTimeField()`를 적용시킨다.
- Movie 클래스는 Review 클래스와 `1:N`관계를 갖는다. 따라서 Review 클래스에는 Movie 클래스와 연결시켜주기 위한 외래키 설정 작업이 필요한데, Django의 models는 이를 위한 ForeignKey 함수를 제공한다.

---

### 2. 페이지

#### 2-0 기본 설정(Basic Settings)

- app에 있는 urls.py의 최상단에는 path와 view모듈을 import한다.

```python
from django.urls import path
from . import views
```

- views.py 상단에 다음 모듈들을 import 한다.

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import MovieForm, RevieForm
```

- app에서 사용할 html 파일 최상단에는 모두 아래 구문을 작성해준다.

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
```

#### 2-1 영화목록(index)

> - 요청 url: `/movies/`
> - url 이름: `index`
> - DB 내 모든 영화의 목록을 `title`, `score`까지만 표시
> - 영화 목록 최상단에 `새 영화 등록` 링크  => `영화 정보 생성 Form`으로
> - 목록 상단에 영화와 관련한 이미지 삽입(Jumbotron, `static`)

```python
# urls.py 설정(요청url과 이름 설정)
path('', views.index, name=index)
```

```python
# views.py index 함수 선언
def index(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'movie/index.html', context)    
```

- Movie 클래스가 갖고 있는 objects 메서드와 all() 함수를 이용해 Movie 클래스가 갖고 있는 모든 데이터들을 가져올 수 있다.
- context로 만들어서 바로 넘겨줄 것이기 때문에, 따로 클래스를 선언 받는 변수를 만들지 않고 html에서 사용될 이름인 'movies'로 바로 넘겨주었다.

```html
<style>
div.jumbotron {
      background-image: url("{% static 'movie-918655_1920.jpg' %}");
      background-position-y: 300px;
    }
</style>
```

- static 경로 설정

```html
{% block body %}
  <div class="row">
    <h1>영화 목록</h1>
    <h5><i>영화 정보 생성은 상단의 링크를 이용해주세요</i></h5>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">글번호</th>
          <th scope="col">영화제목</th>
          <th scope="col">관객평점</th>
        </tr>
      </thead>
      <tbody>
        {% for movie in movies %}
        <tr>
          <th scope="row">{{ movie.pk }}</th>
          <td><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></td>
          <td>{{ movie.score }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
    
{% endblock %}
```

- index.html 페이지는 상단에 적용시킨 {% load bootstrap4 %}를 통해 부트스트랩이 갖고 있는 table component를 적용시켰다. 
- 명세에서 영화제목과 관객평점만을 index 페이지에서 보여주라 하였으므로 Django Template language의 반복문 문법을 사용해 table에 하나씩 담아서 출력해줬다.

#### 2-2 ~ 2-3 영화 정보 생성 Form(Create)

> - 요청 url: `/movies/create/`
> - url 이름: `create`
> - 영화 정보 작성 Form 표시(`ModelForm 활용`)
> - Form Submit 버튼 클릭 시 `영화 정보 생성` 페이지로 생성 요청(`request`)와 함께 전송
> - 전송 받은 데이터의 유효성 검사 실시 후 유효하면 DB에 저장
> - 전송 받은 데이터의 유효성 검사 실시 후 유효하지 않으면 `영화 정보 생성 Form`으로 Redirect
> - 저장이 완료 되면 `영화 정보 조회(Detail)` 페이지로 Redirect

```python
# urls.py
path('create/', views.create, name='create')
```

```python
# views.py
def create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movies = movie_form.save()
            return redirect(movies)
        else:
            return redirect('movies:create')
    else:
        context = {
            'movie_form': MovieForm(),
        }
    return render(request, 'movie/create.html', context)
```

- create 함수로 들어온 요청의 method가 POST이면 Movie의 모델폼을 형성하고 유효성 검사까지 통과하면 movies라는 변수에 저장한다.
- 저장 된 변수 movies를 redirect 함수의 인자로 넣어주면, Movie 클래스에서 만들어준 메소드인 `get_absolute_url`로 인해 detail 페이지로 리다이렉트된다.
- 만약 요청 방식이 POST가 아니면 첫 번째 조건문에서 else쪽으로 가고, html 파일에서 사용할 'movie_form'에 클래스를 선언해주고 create.html 파일을 render하게 된다.
- 요청 방식이 POST라고 하더라도, 유효성 검사를 통과하지 못하면 create 페이지에만 머물게 된다.

```html
{% block body %}
<h1>영화 정보 등록</h1>
<form action="{% url 'movies:create' %}" method="POST">
  {% csrf_token %}
  {% bootstrap_form movie_form %}
  <input type="submit" value="등록" class="btn btn-primary">
</form>
{% endblock %}
```

- form 태그를 통해 form 태그 안에서 일어나는 행위들을 모두 create와 관련된 url로 요청을 보낼 수 있다.
- 부트스트랩에서 제공하는 폼을 활용한다. {%%} 안에서 `bootstrap_form`은은 부트스트랩 속성을 적용시키겠다는 의미, 그 뒤에 오는 movie_form은 `views.py`의 create에서 정의해준 변수.

#### 2-4 영화 정보 조회(Detail)
> - 요청 url: `/movies/<int:movie_pk>/`
> - url 이름: `detail`
> - 해당 Primary Key를 가진 영화의 `모든 정보` 표시
> - detail 페이지 하단에는 `목록(index)`, `수정(Update)`, `삭제(Delete)` 링크가 있음
> - 링크를 누르면 해당 페이지로 이동할 수 있게 구현

```python
# urls.py
path('<int:movie_pk>/', views.detail, name='detail')
```

- Primary Key를 url로 받기 위해서는 위와 같이 url 경로를 설정해주면 된다.

```python
# views.py
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
```

- detail 함수에 요청과 movie_pk에 해당하는 Primary Key가 들어온다.
- 일단 Movie 클래스의 객체들 중, Primary Key가 movie_pk인 객체를 가져와 movies 변수에 저장하는데, 만약 해당하는 값이 없으면 Http404 에러를 띄워주는 식으로 `raise Http404`를 써줄 수 있다.
- `Http404`는 `django.http` 패키지에 있는 모듈들 중 하나이다.
- review_form에는 리뷰와 관련한 모델폼 클래스를 선언해주고
- detail 페이지를 render해서 보여줄 것들을 context로 묶어 detail.html 파이롤 보내준다. 
- `review_set`은 해당 Primary Key를 갖는 객체에 대한 댓글(한줄평)의 모음으로, 자동으로 생성됨.

```html
<!-- detail.html -->
{% block body %}
<h1>영화 상세 정보</h1>
<h3>{{ movies.title }}({{ movies.title_en }})</h3>
<img style="width:30%" src="{{ movies.poster_url }}" alt="">
<p><span>개봉일:</span> {{ movies.open_date }}</p>
<p><span>누적 관객수:</span> {{ movies.audience }}명</p>
<p><span>장르:</span> {{ movies.genre }}</p>
<p><span>관림등급</span> {{ movies.watch_grade }}</p>
<p><span>관객평점</span> {{ movies.score }}</p>
<p><span>줄거리:</span></p><p>{{ movies.description }}</p>

<a href="{% url 'movies:index' %}" class="btn btn-secondary">목록보기</a>
<form action="{% url 'movies:update' movies.pk %}">
  <a href="{% url 'movies:update' movies.pk %}" class="btn btn-info">수정하기</a>
</form>

<form action="{% url 'movies:delete' movies.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="삭제하기" class="btn btn-danger">
</form>

<hr>
<h3>이 영화 한줄평</h3>
<form action="{% url 'movies:create_review' movies.pk %}" method="POST">
  {% csrf_token %}
  {% bootstrap_form review_form %}
  <input type="submit" value="한줄평등록" class="btn btn-success">
</form>
<hr>
  <p style="color: dodgerblue;"><i>전체 {{ reviews | length }}개의 한줄평을 확인해보세요</i></p>
  {% for review in reviews %}
    <p>{{ review.content }} "제 점수는요? <span style="color: gold;">{{ review.score }}</span>점"</p>
  {% empty %}
    <p><i>아직 등록된 한줄평이 없는 영화입니다.</i></p>
  {% endfor %}
{% endblock %}
```

- detail 페이지의 상단에는 Movie의 모델폼 클래스를 통해 생성한 영화에 대한 상세정보들이 들어가 있다.
- 그 아래로 a 태그와 form 태그를 통해 목록, 수정, 삭제 기능을 하는 버튼을 구현해줬고
- 버튼 아래로 Review의 모델폼 클래스를 통해 영화에 대한 한줄평 및 점수를 줄 수 있는 폼을 넣어주었다. 댓글이 입력되면 그래로 댓글과 점수가 최신순으로 보이게 반복문으로 만들어주었다.



#### 2-5 영화 정보 수정 Form(Update)
> - 요청 방식: `GET`
> - 요청 url: `/movies/<int:movie_pk>/update/`
> - url 이름: `update`
> - 해당 Primary Key를 가진 영화 정보 수정이 가능한 Form이 표시되고, `영화 정보 생성Form(Create)`과 동일한 input을 가지고 있다.
> - 작성된 정보를 Form Submit 버튼을 통해 `영화 정보 수정(Update)` 페이지로 수정 요청(request)을 보낼 수 있다.

```html
<form action="{% url 'movies:update' movies.pk %}">
  <a href="{% url 'movies:update' movies.pk %}" class="btn btn-info">수정하기</a>
</form>
```

- detail에서 수정하기 버튼을 누르면 요청이 가게 되는데 이때 요청 보내는 방식은 따로 method를 만들어주지 않아서 디폴트인 GET 방식으로 처리가 된다.

#### 2-6 영화 정보 수정(Update)
> - 요청 방식: `POST`
> - 요청 url: `/movies/<int:movie_pk>/update/`
> - url 이름: `update`
> - 해당 Primary Key를 가진 영화 정보를 이전 페이지로부터 전송 받은 데이터로 변경 후 저장
> - 수정한 영화 정보를 조회하는 `영화 정보 조회(detail)` 페이지로 Redirect

```python
def update(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movies)
        if movie_form.is_valid():
            movie_form.save()
            return redirect(movies)
    movie_form = MovieForm(instance=movies)
    context = {
        'movies': movies,
        'movie_form': movie_form,
    }
    return render(request, 'movie/update.html', context)
```

```html
{% block body %}
<h1>영화 정보 수정하기</h1>
<form action="{% url 'movies:update' movies.pk %}" method="POST">
  {% csrf_token %}
  {% bootstrap_form movie_form %}
  <input type="submit" value="업데이트" class="btn btn-info">
</form>
{% endblock %}
```



#### 2-7 영화 정보 삭제(Delete)
> - 요청 url: `/movies/<int:movie_pk>/delete/`
> - url 이름: `delete`
> - 해당 Primary Key를 가진 영화의 모든 정보를 DB에서 `삭제`
> - 삭제 후 `영화 정보 목록(index)` 페이지로 Redirect

```python
@require_POST
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect(movie)
```

```html
<form action="{% url 'movies:delete' movies.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="삭제하기" class="btn btn-danger">
</form>
```

- 삭제할 때는 url 조작으로 누구나 쉽게 남의 글을 삭제할 수 없도록 POST 방식의 요청이 필수.
- form 태그의 method도 POST로 해주고, delete 함수 위에는 @require_POST라는 데코레이터도 붙여준다.
- @require_POST 데코레이터는 `django.views.decorators.http` 패키지의 모듈 중 하나이다.

#### 2-8 영화 한줄평 생성(Create_review)
> - 요청 URL: `movies/<int:movie_pk>/reviews/`
> - 요청 방식: `Post`
> - 한줄평 작성을 위한 Form은 `영화 정보 조회(datail)`에서 제공
> - `영화 정보 조회(detail)` 페이지로 Redirect

```python
def create_review(request, movie_pk):
    movies = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = movies
            review.save()
    return redirect(movies)
```

```html
<h3>이 영화 한줄평</h3>
<form action="{% url 'movies:create_review' movies.pk %}" method="POST">
  {% csrf_token %}
  {% bootstrap_form review_form %}
  <input type="submit" value="한줄평등록" class="btn btn-success">
</form>
<hr>
  <p style="color: dodgerblue;"><i>전체 {{ reviews | length }}개의 한줄평을 확인해보세요</i></p>
  {% for review in reviews %}
    <p>{{ review.content }} "제 점수는요? <span style="color: gold;">{{ review.score }}</span>점"</p>
  {% empty %}
    <p><i>아직 등록된 한줄평이 없는 영화입니다.</i></p>
  {% endfor %}
{% endblock %}
```

- 댓글 모음 부분을 나름대로 style 속성을 준 span 태그로 꾸며보았다.







