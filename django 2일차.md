# 190813_Django_day_02_오전 수업


## Review

  ```bash
  # 어제 했던던 리뷰. Django로 프로젝트 시작하기.
  $ venv >> 가상환경 시작
  $ mkdir 폴더이름(대문자)
  $ django-admin startproject [프로젝트 이름(소문자)][프로젝트 저장할 폴더이름(대문자)]
  $ python manage.py runserver로 확인
  $ python manage.py startapp [앱 이름]
  ```

  

- 문지기(`url.py`)

  ```python
  from django.contrib import admin
  from django.urls import path
  from pages import views # 이거도 써줘야 함
  urlpatterns = [
      # 첫 번째 인자: 주문서(url 경로)
      # 두 번째 인자: view 함수의 위치
      path('admin/', admin.site.urls),
      path('index/', views.index),    
  ]
  ```
  
- `settings.py > INSTALLED_APPS`
  
  ```python
  INSTALLED_APPS = [
      '[앱 이름]', # 이거를 만들어줘야 한다.
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```
  
- `view.py`

  ```python
  from django.shortcuts import render
    
    # Create your views here.
    def index(request):
        # Flask에서는 render_template('index.html')
        # request 인자에는 사용자가 보낸 요청에 대한 정보가 다 들어있음
        return render(request, 'index.html')
  ```

- root 경로는 빈 스트링으로 만들자(`localhost:8000`만 입력했을 때 보게될 페이지)

  ```python
  path('', views.index) # 두 번째 인자로는 그냥 넣고 싶은 것 넣기
  ```
  
  
## 코드 작성의 원칙: DRY

  - Do not Repeat Yourself
  - 어제 만들었던 페이지들은 동일한 작업을 반복했다.
  - html 틀 만들기. 이 과정을 줄이고 싶으면? `==>` 상속!
  - 상속
    - 공통적으로 쓸 템플릿(코드)을 뽑아낸다.
    - 해당 파일을 따로 만들고,
    - 활용할 다른 템플릿 파일에서 불러와 쓴다.
  - Django + bootstrap
    - navbar, footer, body 등, 여러 템플릿에 공통적으로 쓰이는 코드를 따로 저장하여 템플릿 상속을 통해 반복되는 코드를 줄일 수 있다.
      1. 공통적으로 쓰이는 코드를 따로 저장한다
      2. 해당 파일을 따로 만든다.
      3. 활용할 다른 템플릿 파일에서 불러온다.

  ```html
  <!--반복 사용될 부분-->
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
      integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
      integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
    <title>Document</title>
  </head>
  
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">잡동사니</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/cube/3">세제곱계산기</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/lotto/">로또</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/home/">DTL 정리</a>
          </li>
        </ul>
      </div>
    </nav>
    {% block body %}
    {% endblock %}
  </body>
  
  </html>
  ```

  ```html
  <!-- base가 될 html파일(재사용할 것)에 빈 구멍을 뚫어주는 느낌. -->
  <!-- 템플릿을 만들고 새로운 것들을 넣어줄 곳에 block을 뚫을 건데 그 이름을 body로 지은 것-->
    {% block body %}
    {% endblock %}
  </body>
  
  </html>
  ```

### {% extends 'base.html' %}

- `base.html`에 저장된 템플릿 페이지를 불러온다(extend: '확장시키다')
- 어제 만든 `localhost:8000/index/`를 보여줄 html 파일을 base.html에 적용시키고 싶으면?
- index.html 파일을 열고, `<body> 태그 안에 있는 내용물`만 남겨두고 지운다
- 그렇다면, index.html 파일에는, body 안에 있던 contents 만 남게 된다.
- contents 상단에 `{% extends 'base.html' %}`을 써준다.
- 그리고 남아 있던 contents를 `{% block body %} contents {% endblock %}`로 감싸준다.
  - base.html에 있는 `{% block body %} {% endblock %}'` 사이에 contents를 넣어주겠다는 의미.

  ```html
<!-- base.html 파일의
     block body 부분에
     아래 contents를 넣어주겠다는 의미-->

  {% extends 'base.html' %}

  {% block body %}
  <h1> DTL(Django Template Language) 관련 문법 </h1>
    <ul>
      <li>for</li>
      <li>if</li>
      <li>helper</li>
      <li></li>
    </ul>
  
    <h2>데이터를 넘겨받는 법</h2>
    <p> {{ name }}</p>
    {% for item in data %}
    <p>{{item}}</p>
  
    {% endfor %}
  
  
    <h2>for문 활용법</h2>
    <!-- <h2>데이터가 없을 때</h2> -->
    {% for movie in empty_data %}
      <p>{{ forloop.counter }} : {{ movie }}</p>
    {% empty %}
    <p>영화 데이터가 없습니다.</p>
  
    {% endfor %}
  
  
    <h2>이중 for문</h2>
    {% for array in matrix %}
      {% for num in array %}
        <p>{{ num }}</p>
      {% endfor %}
    {% endfor %}
  
    <h2>다양한 helper / filter</h2>
    <h3>helper</h3>
    <!--Displays random “lorem ipsum” Latin text. This is useful for providing sample data in templates.-->
    {% lorem 3 p random %}
  
    <h3>filter</h3>
    {% for movie in empty_data %}
      {{ movie|length }}
      <!-- movie에 들어간 영화 제목의 길이를 출력-->
      {{ movie|truncatechars:3 }}
      <!-- movie에 들어간 영화 제목의 길이를 3(세자리)까지만 표시-->
    {% endfor %}
  
    <h4>int</h4>
    {{ number|add:90 }}
  
    <h4>datetime</h4>
    {% now 'Y년 M월 m월 d일 h시 i분 a day' %}

  {% endblock %}
  ```



# 190813_Django_day_02_오후 수업

## 한 단계 더 나가보자
- footer랑 nav의 템플릿들도 만들어볼 수 있다. `partial template`
- `first_app > templates 폴더`에 `_footer.html`과 `_nav.html`을 만들어주자.
- 파일명 앞에 under-bar를 붙여주는 것이 관례
- 그러면 `_nav.html`과 `_footer.html`을 불러오려면 `{% extends '_nav.html' %}`이나 `{% extends '_footer.html' %}`로 될까?
- 안된다. 왜? 사용할 수 있는 문법이 다르기 때문.

### {% include '파일명' %}
- 문제들을 기능별로, 로직별로 그 부분에만 국한시켜 해결할 수 있게 된다.

  ```html
  <body>
    <!-- _nav.html 파일 갖고 오기-->
    {% include '_nav.html' %}
  
    {% block body %}
    {% endblock %}
  
    <!-- _footer.html 파일 갖고 오기-->
    {% include '_footer.html' %}
  
  </body>
  ```

  ```html
  <!-- _nav.html 파일-->
  <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
    <a class="navbar-brand" href="#">잡동사니</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
      aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/cube/3">세제곱계산기</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/lotto/">로또</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/home/">DTL 정리</a>
        </li>
      </ul>
    </div>
  </nav>
  ```

  ```html
  <!-- _footer.html 파일-->
  <footer class="d-flex fixed-bottom justify-content-center">
    <p>Made by Kahn</p>
  </footer>
  ```



### Django스럽게 아스키 아트 앱을 만들어보자
- Django스럽다 `==` 중복된 코드 사용을 하나로 묶어버린다.
- 어제 만든 `pages 앱`과 오늘 만든 `artii 앱`에서 공통으로 사용하는 templates들을 묶어버리자.
  - `base.html`은 html의 body를 담는 공통 템플릿
  - `_footer.html`은 html의 footer를 담는 공통 템플릿
  - `_nav.html`은 html의 navbar를 담는 공통 템플릿

- first_app 프로젝트 폴더에 `templates` 폴더를 만들어서 공통 템플릿을 옮겨준다.

  - 그러면 이제 바꿔줘야할 부분이 생긴다.

  - 공통템플릿을 사용하는 pages의 html은 템플릿을 찾을 수 없다는 에러가 화면에 보이게 된다.

  - FIRST_APP 프로젝트의 first_app 폴더 안의 settings.py에서 TEMPLATES 부분을 다음과 같이 수정하자.

  - `TEMPLATES` 리스트 요소인 딕셔너리에서, `DIRS`라는 key의 value로 `[os.path.join(BASE_DIR, 'first_app','templates')]` 리스트 추가
  
  - 무슨 뜻인지는 나중에 이해하기.
  
    ```python
    import os
    
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'first_app','templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
          },
        },
  ]
    ```

### artii 앱 만들기
- 사용자의 input을 받는 url
  - /artii/
  - (추가) 폰트 선택 창을 만들어보자.
  
- artii API를 통해 ascii art를 보여주는 url 
  
  - /artii/result/
  
- Git Bash에서 `pip install requests` 해주기. (지금 venv 가상환경에서 작업 중이라 이전에 깔았던 requests는 3.5버전에서만 존재하고 있기 때문.)
  ```bash
  $ pip install requests
  ```
  
- 새로운 artii 프로젝트 앱을 만들자
  ```bash
  $ python manage.py startapp artii
  ```
  
- /first_app/settings.py의 INSTALLED_APPS 에서 새로 만든 앱 이름을 추가해 주자
  ```python
    INSTALLED_APPS = [
        'artii',    # 오늘 만들 artii 앱
        'pages',    # 어제 프로젝트에서 만든 pages 앱
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
  ]
  ```
  
  
  
- `urls.py`에서 새로운 경로 2개를 지정해주자(입력url, 결과url)
  
    ```python
    from django.contrib import admin
    from django.urls import path
    from pages import views
    from artii import views as artii_views
    # views는 어제 만들 때 이미 존재하는 이름이므로 as를 통해 이름을 바꿔준다.
    
    urlpatterns = [
        path('', views.index),
        path('admin/', admin.site.urls),
        path('artii/', artii_views.artii),    # 사용자의 입력을 받을 곳
        path('artii/result/', artii_views.artii_result), # 사용자가 입력한 것의 결과물을 보여주는 곳
    ]
    ```
    
    ```python
    # 이 과정이 번거롭다면, artii 폴더 안에 아예 따로 urls.py를 만들어주자
  from django.urls import path
  from . import views
  # .은 현재 폴더를 의미함.
  # 새로 만들어준 지금 이 urls.py 파일은 artii 폴더에서 views.py와 같이 있음.
  
  urlpatterns = [
      path('', views.artii),
      path('result/', views.artii_result)
      # 위에처럼 번거롭게 views의 새 이름을 쓰지 않아도 된다.
  ]
  ```
  
  
  
- 입력url(`localhost:8000/artii/`)에서 보여줄 html페이지에 표시할 기능들을 `views.py`에 만들어 주자.
  
  ```python
  from django.shortcuts import render
  
  def artii(request):
      import requests
      font_url = 'http://artii.herokuapp.com/fonts_list'
      response = requests.get(font_url).text
      font_list = response.split()
      context = {
          'font_list': font_list,
    }
    return render(request, 'artii/artii.html', context)
  ```
  
  
  
- 사용자의 입력을 받을 `artii.html 파일`을 만들어준다.
  
  - `artii.html`에서는 사용자가 입력할 공간을 form 태그를 통해서 만들어준다.
  - form태그의 action 속성: 사용자가 제출을 누르면 `/artii/result/`로 가게 해준다.
  
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>my_artii</title>
    </head>
    <body>
      <form action="/artii/result/">
        <input type="text" name="string"><button type="submit">제출</button>
      </form>
    </body>
  </html>
  ```
  
  
  
- 결과url(`localhost:8000/artii/result`)에서 보여줄 html페이지에 표시할 기능들을 `views.py`에 만들자.

    ```python
    def artii_result(request):
        import requests
        
        # 1. 단어를 받아온다. request.Get.get('string')
        string = request.GET.get('string')
        font = request.GET.get('font')
        
        # 2. artii api를 통해 ascii art 결과물을 요청하고.
        url = f'http://artii.herokuapp.com/make?text={string}&font={font}'
        result = requests.get(url).text
        
        # 3. 결과를 받아와 보여준다.font_url = f'http://artii.herokuapp.com/make?text={string}'
        context = {
            'string': string,
            'artii_result': result,
        }
        return render(request, 'artii/artii_result.html', context)
    ```

    

- 결과물을 표시해줄 `artii_result.html` 페이지를 만든다.
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>my_artii_result</title>
    </head>
    <body>
      {{ artii_result }}
    </body>
  </html>
  ```

### 현재 폴더 구조

```python
FIRST_APP >							# 프로젝트 이름
	first_app >						# 프로젝트의 기본적인 셋팅과 공통 템플릿 관리				
		settings.py					# 공통 템플릿 경로 설정
		urls.py					    # pages나 artii에서 사용할 url 설정
		templates >					# 공통 템플릿은 이곳에 뽑아서 둔다.
			_footer.html				{% include '_footer.html' %}
			_nav.html					{% include '_nav.html' %}
			base.html					{% extends 'base.html' %}
	pages >							# day01에 만든 app
		views.py					# pages 앱이 보여줄 templates의 기능
		templates >					# 사용자에게 보여줄 페이지 저장
			cube.html
			home.html
			index.html
			lotto.html
			match.html
	artii >							# day02에 만든 app
		urls.py						# pages의 views와 겹치지 않게 따로 설정 가능
		views.py					# artii 앱이 보여줄 templates의 기능
		templates >					# 사용자에게 보여줄 페이지들 저장
			artii >					# 중복을 방지하기 위한 폴더 depth 설정
				artii.html
				artii_result
```



