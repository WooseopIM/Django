# 190820

## 오전수업 - CRUD 프로젝트 만들기

> Create, Read, Update, Delete

### CRUD 프로젝트 생성 미션!

- STEP 1. `CRUD 프로젝트 생성` / `articles 앱 생성`

  - ```bash
    $ venv
    $ mkdir CRUD
    $ django-admin startproject crud CRUD
    $ cd CRUD
    $ python manage.py runserver
    $ ^C
    $ python manage.py startapp articles
    ```

- STEP 2. 

  - `/articles/new`: `form`을 통해 사용자들로부터 `title`과 `contents`를 입력 받음

  - `/articles/create/`: GET 방식으로 데이터를 보내어 처리. DB에 글을 저장 & Redirect to '/'

  - `articles.views.index`: index.html 에서는 지금까지 쓴 글들을 볼 수 있는 페이지를 만들자.

  - ```python
    # crud.settings.py
    INSTALLED_APPS = ['articles', ... ]
    
    # crud.urls.py
    from django.contrib import admin
    from django.urls import path, include
    from articles import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
        path('', views.index, name="index"),
    ]
    ```

  - ```python
    # articles.urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('',views.index),
        path('new/', views.new),
        path('create/', views.create),
    ]
    ```

  - ```python
    # articles.models.py
    from django.db import models
    
    class Articles(models.Model):
        title = models.TextField()
        contents = models.TextField()
        img_url = models.TextField()
    
        def __str__(self):
            return f'{self.id} : {self.title}'
    ```

  - ```python
    # articles.views.py
    
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
    ```
    

  

  - base.html 만들기

  - ```html
    <!doctype html>
    <html lang="en">
    
    <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
      <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <link rel="stylesheet" href="style.css">
      <link href="https://fonts.googleapis.com/css?family=Jua|Sunflower:300&display=swap" rel="stylesheet">
      <title>CRUD Practice</title>
    </head>
    
    <body>
      {% include '_nav.html' %}
      {% include '_jumbotron.html' %}
    
      {% block body %}
    
      {% endblock %}
    
      {% include '_footer.html' %}
    
      <!-- Optional JavaScript -->
      <!-- jQuery first, then Popper.js, then Bootstrap JS -->
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
      </script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
      </script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
      </script>
    </body>
    
    <style>
      * {
      font-family: 'Jua', sans-serif !important;
    }
    .jumbotron {
      background-image: url('https://static1.visitestonia.com/images/2890339/Estonian_forest_reasons_to_visit_Sven_Zacek.jpg') !important;
      background-position-y: 300px;
    }
    
    h1 {
      color: aliceblue;
    }
    
    </style>

    </html>
    ```
    

  

  - {% include 'html 파일' %}를 통해 쓸 것들

    - {% include '_nav.html' %}

    - ```html
      <nav class="navbar navbar-expand-lg navbar-light bg-success d-flex">
          <a class="navbar-brand" href="#">CRUD Practice</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item active">
                <a class="nav-link" href="#">Home<span class="sr-only">(current)</span></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">아무것도연결안된링크</a>
              </li>
            </ul>
          </div>
        </nav>
      ```

    - {% include '_jumbotron.html' %}

    - ```html
      <div class="jumbotron jumbotron-fluid d-flex" id="Top_page">
          <div class="container text-center">
            <h1 class="display-4">넌 이미 야자를 하고 있다</h1>
            <p class="lead" style="color: aliceblue">... 하지 않겠는가? </p>
          </div>
      </div>
      ```

    - {% include '_footer.html' %}

    - ```html
      <footer class='bg-success fixed-bottom'>
          <div class="row" style="justify-content:space-around; line-height: 50px">
            <span style="color: aliceblue">ⓒ2019,Kahn</span>
            <span><a href="#Top_page"><button class="btn btn-info">Top</button></a></span>
          </div>
      </footer>
      ```

  - `base.html` 템플릿을 적용시킬 `index.html`, `new.html`

  - ```html
    {% extends 'base.html' %}
    
    {% block body %}
    <div class="container">
      <h1 style="color: black">쓴 글 목록<a type="button" class="btn btn-info" href="articles/new/">새 글쓰기</a></h1>
      <div class="row">
        {% for article in articles %}
        <div class="card w-50">
          <div class="card-body">
            <h5 class="card-title">제목: {{ article.title }}</h5>
            <p class="card-text">내용: {{ article.contents }}</p>
            <p>이미지: <img src="{{ article.img_url }}" style="width: 100%" alt=""></p>
          </div>
        </div>
        {% endfor %}
      </div>
    
    </div>
    
    {% endblock %}
    ```

  - ```html
    {% extends 'base.html' %}
    
    {% block body %}
    <div class="container">
      <h1>CRUD 실습 블로그를 만들어보자</h1>
    
      <form action="/articles/create/" method="GET">
        <label for="">제목</label>
        <input class="form-control" type="text" name="title" placeholder="제목을 입력하세요" style="width: 60%"><br>
        <label for="">내용</label>
        <textarea class="form-control" name="contents" cols="50" rows="10" placeholder="내용을 입력하세요" style="width: 60%"></textarea><br>
        <label for="">이미지url</label>
        <input class="form-control" name="img_url" type="text" style="width: 60%">
        <a class="button btn btn-secondary" href="">업로드</a>
        <button class="btn btn-secondary" type="submit"></button>
      </form>
    </div>
    
    
    {% endblock %}
    ```

  - `bash terminal`에서 마무리 하고 확인

  - ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
    ```

  - 끝!



- 전체적인 Work flow
  - Model을 먼저 잡고
  - url > view > template 순으로 조진다.
- text가 적게 들어올 때는 models.TextField보다는 models.CharField를 써서 메모리 데이터를 효율적으로 쓰게 하자. CharField는 max_length를 인스턴스로 받는다.



## 오후수업 - SSAFY 서울1반 BOARD 프로젝트 만들기

### APP 추가하기

- posts라는 app을 만들어줬으므로, settings.py의 INSTALLED_APP에 'posts'를 추가해준다.

- ```python
  # board.setting.py에서
  INSTALLED_APPS = ['articles', ... ]
  ```



### Model 만들고 상속시키기 / Migration

- 항상 Database의 Model을 먼저 기획하고 시작하는 습관을 들이자.

- model.py는 우리가 만들 DataBase의 설계도라고 할 수 있다.

- **까먹지 말고 class에 django가 만들어 놓은 models.Model을 상속 시킨다.**

- Post는 models.Model 클래스를 상속받은 클래스. Model가 갖고 있는 다양한 Field 속성들을 적용시킬 수 있다. 여기서 내가 원하는 것들(예: 작성자, 태그, 추천수, 댓글 등)을 만들어가면 된다. 단, 이미 makemigrations가 끝난 이후 DB에 추가하게 된다면 makemigrations를 한 번 더 해줘야 한다.

- ```python
     from django.db import models
     # DB 설계도를 만들었으면 makemigrations
     
     class Post(models.Model):
         title = models.CharField(max_length=100)
         content = models.TextField()
         image_url = models.CharField(max_length=300)
         created_at = models.DateTimeField(auto_now_add=True) 
         updated_at = models.DateTimeField(auto_now=True)
         # 작성자 = 
         # 태그 = 
         # 조회수 = 
         # 추천수 = 
         # 좋아요 = 
         # 댓글 = 
     ```

- model.py에서 전체적인 틀을 짰으면, Git Bash 터미널에서 migrate 과정을 해준다.

- ```bash
     $ python manage.py makemigrations
     $ python manage.py migrate
     ```



### URL 정의하기(`board의 urls.py`)

- `board.urls.py`에서 앞으로 우리가 사용할(사용자의 요청을 처리할) URL들에 대한 정의를 해주자.

  - 메인페이지(홈페이지): 사용자들이 입력한 제목, 내용, 이미지URL 등의 내용을 list로 보여주는 홈페이지를 root페이지로 만들기 위해 경로를 `''`로 설정해주고, 나중에 사용하기 편리하게 이름을 `home`이라고 붙여주자.

  - 앞으로 들어올 모든 url은 `root url` + `posts/~~`의 형식을 갖게될 것이므로, 

  - post app에서 관리하는 `urls.py`로 보내기 위해 `include`시킨다.

  - django.urls가 갖고 있는 include를 import하는 걸 까먹지 말자.

  - ```python
    from django.contrib import admin
    from django.urls import path, include 
    from posts import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name='home'),
        path('posts/', include('posts.urls')),
    ]
    ```



### 공통 템플릿 만들기(`board의 templates 폴더`)

- 사용자가 보는 화면에 항상 보여질 모습 즉, 공통 템플릿을 만들자

  - 이번 프로젝트에서는 bootstrap의 navbar가 공통으로 적용된 base.html이라는 템플릿을 만들 것

  - navbar에 대한 것도 효율적으로 관리를 하려먼 `_nav.html`파일을 만들어 `base.html`에 `{% include '_nav.html' %}` 이런 식으로 활용할 수 있다.

  - `base.html`: bootstrap의 CDN이 적용된 베이스 템플릿이다.

    ```html
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
        <title>SSAFY BOARD</title>
      </head>
      <body>
        {% include '_nav.html' %}
    
        {% block body%}
        {% endblock %}
    
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
      </body>
    </html>
    ```

  - `_nav.html`: bootstrap의 `navbar` 컴포넌트만 따로 관리하려면 따로 html파일을 만들어 관리해줄 수 있다.

  - 만들고 `base.html`의 `<body>태그` 안에 {% include %}로 삽입해주자.

    ```html
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">SSAFY 게시판</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="{% url 'posts:new' %}">새글쓰기</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
        </ul>
      </div>
    </nav>
    ```
    - 이렇게 해주면 `settings.py`에서 바꿔줘야 하는 부분이 생긴다.




### 공통 템플릿 탐색하기(`board의 settings.py 수정`)

- django는 기본적으로 templates 탐색 할 때, 각 app에 있는 templates만 탐색한다.
- 우리는 공통템플릿을 관리하기 위해 메인 프로젝트 폴더인 board에 templates를 만들어줬으니까
- django한테 이 templates도 탐색하라고 명령을 만들어줄 필요가 있다.
- `settings.py`에서
- `'DIRS': [os.path.join(BASE_DIR, 'board', 'templates')]`: BASE_DIR(BOARD) > board > templates를 탐색하라는 의미

- ```python
  # board의 settings.py에서
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  
  TEMPLATES = [
      {    ...
          'DIRS': [os.path.join(BASE_DIR, 'board', 'templates')],
       	...
      },
  ]
  ```



### posts app에 따로 urls.py 만들어주기


  - /posts/~~ 로 들어오는 url을 처리하기 위해 `board의 urls.py`에서 `include('posts.url')`을 해줬다.

  - 이것을 받아줄 urls.py를 posts app 안에 만들어줘야한다.

  - ```python
    from django.urls import path
    from . import views
    '''
    여러 app별 중복 이름 사용을 위한 app_name 설정
    함수 이름으로 new나 create 등을 중복해서 사용하게 될 일이 있을 건데
    그 때마다 'posts_new' 이런 식으로 app이름을 붙여 함수명을 길게 만들어주는 것을 방지하기 위해서
    아래와 같이 app_name을 설정해준다.
    '''
    app_name = 'posts'
    
    urlpatterns = [
        path('new/', views.new, name='new'),
        path('create/', views.create, name='create'),
        path('<int:pk>/', views.detail, name='detail'),
        path('<int:pk>/delete/', views.delete, name='delete'),
        path('<int:pk>/edit/', views.edit, name="edit"),
        path('<int:pk>/update/', views.update, name="update"),
    ]
    ```

  - 지금은 posts라는 app 하나만 있기 때문에 상관 없지만, 앞으로 django 프로젝트를 함에 있어서 동일한 이름의 함수들을 각 app별 views.py에 만들게 될 것이다.

  - 이 때, 각 app에서 서로 같은 기능을 하는 함수를 동일한 이름으로 만드는 것이 편할 것이다.

  - 왜냐하면 이름을 여러개 만들지 않아도 되기 때문이다.

  - 동일한 이름의 함수가 있을 때, 이 중에 한 함수를 html파일 등에 적용시킬 때, 어떤 app으로부터 왔는지 구분하기 위해 app_name이라는 namespace 변수 선언을 사용한다. `posts:new` 이런 식으로 활용.

  - 이렇게 해주면 모든 함수마다 일일이 해당 앱의 이름을 붙인 함수명을 만들어주지 않아도 된다.

  - 달라지는 url을 만들고 싶으면 <>를 활용하면 된다.



### posts 앱 템플릿들(`posts/templates/posts 안에 만들기`)

- 사용자에게 보여질 앱 템플릿의 폴더 트리는 posts(app) > templates > posts로 구성한다.
- django가 templates 탐색을 할 때, 여러 app이 있을 때는 모든 app들의 templates를 탐색하기 때문인데, 동일한 이름의 html 파일을 찾을 때 혼동을 주지 않기 위해서 폴더의 Depth를 설정하는 것이다.



### 이제 본격적인 CRUD 기능을 하는 `views.py`를 조져보자 (+`html`)

- CRUD: Create, Read, Update, Delete

- ```python
  # 앞에 까먹지 말고 꼭 붙여주자
  from django.shortcuts import render, redirect	# django가 기본적으로 붙여주는 부분
  from .models import Post
  # 우리가 만든 Post Class를 불러오는 부분 from의 .model의 의미는 현재 views.py와 동일한 계층(같은 폴더 내)에 있는 models.py라는 패키지에서 우리가 만들어준 Post Class를 가져다 쓰겠다는 의미이다.
  ```

- `index(메인페이지)`

  - table(표) 형태로 사용자가 업로드한 게시글을 보여주는 홈페이지

  - table의 형식은 bootstrap에서 제공하는 형식을 사용할 것이다.

  - 우리의 메인페이지(root page)로 사용될 것이다.

  - 앞에서 url 설정할 때 별명(name)을 'home'으로 설정해준 이유

  - ```python
    def index(request):
        # table 형태로 게시판을 보여줌(Bootstrap으로 설정)
        # 메인페이지이므로 모든 것들을 보여주려면 다음과 같이 선언해준다.
        posts = Post.objects.all()
    
        context = {
            # DB에 있는 모든 데이터 들고 오는데, 최신글이 위에 오도록(reversed)
            # 앞에 key로 사용된 posts는 html에서 사용될 이름
            'posts': reversed(posts)
        }
        return render(request, 'posts/index.html', context)
    ```

  - 주의할 점! 앞서 html 파일을 만들어 줄 Depth를 설정해줬으므로 render할 html파일의 위치를 잘 지정해주는 것이 필요하다. templates의 posts 폴더에 만들어줬으므로 `posts/~~`를 붙여준다.

  - ```html
    {% extends 'base.html' %}
    {% block body %}
    <div class="container">
      <div class="row">
        <h1>SSAFY 서울 1반 게시판</h1>
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">글번호</th>
              <th scope="col">제목</th>
              <th scope="col">생성일</th>
              <th scope="col">수정일</th>
            </tr>
          </thead>
          <tbody>
            {% for post in posts %}
            <tr>
              <th scope="row">{{ post.id }}</th>
              <td><a href="/posts/{{ post.id }}">{{ post.title }}</a></td>
              <td>{{ post.created_at }}</td>
              <td>{{ post.updated_at }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    
    {% endblock %}
    ```

  - `index` 함수에서 만들어준 html 파일

  - 화면에서 보기 좋게 container 클래스와 row 클래스가 적용된 Bootstrap의 table을 만들어준다.

  - 반복되는 부분은 `{% for post in posts %}`를 통해 코드의 사용성을 높인다.

  - ```html
    {% for post in posts %}
    <tr>
        <th scope="row">{{ post.id }}</th>
        <td><a href="/posts/{{ post.id }}">{{ post.title }}</a></td>
              <td>{{ post.created_at }}</td>
              <td>{{ post.updated_at }}</td>
            </tr>
            {% endfor %}
    ```

  - 

- `new`

  - 사용자로부터 새로운 글을 쓸 수 있도록 만들어주는 부분이다.

  - `views.py`에서는 따로 만들어 줄 것은 없고, html 경로 설정만 주의해주면 된다.(`posts/` 꼭 붙여주기!)

  - ```python
    def new(request):
        return render(request, 'posts/new.html')
    ```

- `create`

  - new에서 날아온 데이터를 DB에 저장하기 위해 만들어준 기능

  - 따로 html 페이지를 render할 필요가 없으므로 메인페이지(홈)로 redirect 시키는데, 앞서 설정한 별명인 'home'을 이용하여 간단하게 홈페이지로 redirect 시킨다.

  - 여러 기능들 중 한가지를 선택해서 쓰도록 하자. 각각에는 장단점이 있다.

  - ```python
    # 1번
    def create(request):
        post = Post(
            title = request.GET.get('title'),
            content = request.GET.get('content'),
            image_url = request.GET.get('image_url'),
        )
        post.save()
        return redirect('home')
    ```

  - ```python
    # 2번-save 기능을 포함한 create메서드 사용
    def create(request):
        Post.objects.create(
            title = request.GET.get('title'),
            content = request.GET.get('content'),
            image_url = request.GET.get('image_url'),
        )
        return redirect('home')
    ```

  - ```python
    # 3번 - DB에 들어간 Column명과 input에 붙인 데이터의 name이 같을 때 다음과 같이 한 줄로 쓸 수 있다. 전부 긁어오는 것이기 때문에 불순물 데이터를 긁어오는 것을 방지하고 선택적으로 원하는 값들만 가져오기 위해서는 2번 기능을 쓰면 된다.
    def create(request):
        Post.objects.create(**request.GET.dict())
        return redirect('home')
    ```

- `detail`

  - 메인페이지에서 글의 제목을 클릭했을 때 상세 내용을 보여주는 기능을 한다.

  - django에서는 primary key라는 의미의 pk를 사용할 수 있다.

  - pk라는 id를 가진 글을 찾아와 보여준다.

  - id는 우리가 따로 model에서 만들어주지 않아도, django가 자동으로 만들어주는 부분이다.

  - ```python
    def detail(request,pk):
        post = Post.objects.get(pk=pk)
        context = {
            'post': post
        }
        return render(request, 'posts/detail.html', context)
    ```

- `delete`

  - 글을 삭제하는 기능

  - pk라는 id를 가진 글을 삭제한다.

  - 일단 삭제할 글의 id를 찾기 위해 detail에서와 같은 방식을 사용한다.

  - 삭제할 때는 `.delete()`를 쓰자

  - ```python
    def delete(request,pk):
        post = Post.objects.get(pk=pk)
        # 삭제하자!
        post.delete()
    
        return redirect('home')
    ```

#### 글을 수정(update)하는 것은 삭제보다는 번거롭다.

- 수정은 `편집 -> 업데이트`의 `2 steps`을 가진다.

- `edit`

  - 사용자가 '수정' 버튼을 누르면, edit이라는 url이 생성된다.

  - pk라는 id를 가진 글을 편집하게 하기 위해서 pk라는 id를 가진 글을 찾는다.

  - django에서는 id를 의미하는 pk key를 갖고 있다.

  - ```python
    def edit(request,pk):
        post = Post.objects.get(pk=pk)
        context = {
            'post': post,
        }
    
        return render(request, 'posts/edit.html', context)
    ```

- `update`

  - `edit` url에서 해당하는 글을 찾았다면 그 글을 수정하고 보내는 요청을 `update` url로 만든다.

  - pk라는 id를 가진 글을 찾아서, `edit`으로부터 날아온 데이터를 수정 대상으로 적용하여 변경한다.

  - 따로 보여질 페이지는 만들 필요 없이, 수정하고나면 수정된 detail 페이지를 보여준다.

  - ```python
    def update(request, pk):
        post = Post.objects.get(pk=pk)
        post.title = request.GET.get('title')
        post.content = request.GET.get('content')
        post.image_url = request.GET.get('image_url')
        post.save()
    
        return redirect('posts:detail',pk)
    ```

  - 