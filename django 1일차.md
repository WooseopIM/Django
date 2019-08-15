# 190812_django_day_01_오전 수업
## Django Intro

- 여러 웹 프레임워크 중 `Opinionated`, `Unopinionated` 성격을 모두 갖고 있음
  - 장고에서 정한 규칙대로 따라야 하는 `opinionated(독선적) 성격`. 초반에 배워야할 게 많지만 배워두면 이후부터 뭔가를 할 때 편해짐
  - 우리가 원하는대로 짜게 해줄 수 있는 `Unopinionated` 성격도 있지만, 기능등이 잘 모듈화되어있지 않기 때문에 나중에 코드의 유지관리/보수가 힘들 수도 있음
  - 초반에는 장고가 정해둔 규칙을 익히는 데 시간을 많이 쓰게된다.
  - `장고?` `쟁고?`, `디장고?`, `디쟁고?`
  
- 지금까지 우리가 만든 웹은 github page를 통해서 Static Web이었다.
  - 모든 사람들에게 동일한 컨텐츠를 배포하는 웹
  - 우리는 장고를 통해 Dynamic web을 만들 것(User와 상황마다 다른 컨텐츠를 제공)
  - 웹 서비스를 만드는 것 `==` 카페를 창업하는 것
  
- 카페를 창업하는 두 가지 방법? (Flask할 때도 설명)
  - A-Z 모두 직접 하기(홍보/마케팅, 인테리어, 레시피개발, 원자재 확보, 매출 정산, 등등...)
  - 프랜차이즈 창업
  
- 웹 서비스를 제작하는 두 가지 방법?
  - A-Z 모두 직접 하기: URL Parsing, DB Setting, Security... Caching... Web Server Setting....
  - Framework 사용: 프랜차이즈 카페를 창업하듯이 자잘한 귀찮은 것들을 맡기고 우리는 우리가 원하는 핵심 로직만 만들면 된다.
  
- 기본적인 레시피나, 필요한 재료는 알아서 제공해줄테니, 좋은 카페를 만드는 것에 집중해라!

- 기본적인 구조나, 필요한 코드들은 알아서 제공해줄테니, 좋은 웹 서비스를 만드는 것에 집중해라!

- 그렇다면 hotframwork에는 어떤 것들이 있나?
  - Express JS
  - Ruby on Rails
  - Python django: 파이썬에서는 장고가 제일 유명! 서로 뗄 수 없는 관계.
  - PHP laravel
  - Java Spring

- 장고는 이미 많은 회사들이 쓰고 있다: `유튜브`, `인스타그램`, `moz://a`, `NASA`

- 파이썬은 이미 전사적으로 대세가 되는 분위기. 

- Flask 를 이용했던 간단한 웹 만들기
  ```python
  @app.route('posts')
  def index():
      ...
      return render_template
  ```
- 그러나 flask로 구현하려는 웹 기능이 많아지면 많아질 수록 관리하기 불편해졌다.
  ```python
  posts/
  posts/create
  posts/edit
  posts/delete
  .
  .
  .
  # 각 페이지마다 따로 만들어줘야했기 때문.
  ```
  
- MVC, MTV
  - 아름답게 코드 유지/보수/관리 가능한 패턴
  - 장고를 쓰기 위해서는 반드시 MVC 패턴을 익혀야 한다.
  - 그런데 장고에서는 MVC를 MTV라고 명명. 기본은 똑같다.
  - `M`odel(데이터 `관리`)/`T`emplate(사용자가 `보는 화면`)/`V`iew(`중간 관리자`)
  - 1~2주차에는 T와 V에 집중, 데이터베이스를 익힌 후에는 M에도 집중하게될 것
  - 이 중에서 가장 중요한 것은 중간 관리자인 `View!`

- Django의 요청 처리 방식
  - `View`가 `Model`과 `Template`을 관리한다.
  - Step by step으로 알아보자.
    1. 사용자가 url 입력 (요청이 들어온다.)
    2. _(문지기가 view한테 전달): 지금은 몰라도 되는 과정_
    3. `view`가 `model`한테 database에서 사용자가 원하는 자료를 찾으라고 명령
    4. `model`은 database에서 요청한 자료를 찾아 `view`한테 넘김
    5. `view`는 다시 그 문서를 `template`한테 넘긴다.
    6. `template`은 html 페이지를 사용자에게 보여줌!





## Django 프로젝트 시작해보기 1

### Intro

- SSAFY 컴퓨터로 작업할거면 3.7버전 이상의 파이썬 virtual env(가상환경)에 django 2.2.4 최신 버전을 install해서 작업하자 (알고리즘은 파이썬 3.5버전을 써야함)

- 장고의 관례에 맞춰 맨날 똑같이 쓰는 파일의 템플릿을 만들자: `git bash창 켜기`
  ```bash
  $ venv: 미리 만들어 둔 가상환경 setting 
  $ django-admin startproject [first_app: 프로젝트 이름] [FIRST_APP: 디렉토리]
  ```
  
  - 폴더구조[디렉토리]는 대문자로, 동일한 이름의 프로젝트를 소문자로 작성한다.
  - 뭔가 생겼다!? (first_app 폴더랑 manage.py)

  - first_app 폴더 안에도 뭔가가 생겼다!
  ```bash
  $ python manage.py runserver
  ```
  - 서버를 돌련 후, 브라우저에 `localhost:8000` 입력하고 들어가서 장고로켓이 보이면 된 것! 서버 끄는 방법은 Flask 랑 똑같이 `Crtl+C`

- 장고 프로젝트의 디렉토리 컨벤션(폴더 하부 구조):

  - 장고 전체 크기 구조를 Project라는 이름으로 부를 것
  
  - 이 프로젝트 안에 세부적인 기능을 하는 app들이 들어올 것이다.
    - FIRST_APP: 폴더 아래에는 로직 별로 기능이 분화된 app들이 있음
      - `first_app`: 처음 만든 테스트 app
      - `app1`: 게시판 관리 기능 app
      - `app2`: 회원 관리 기능 app
      - `app3`: 영화 평점 기능 app
      .
      .
    
  - 지금 만든 것은 첫 app이라는 의미로, `first_app`이라는 앱을 만들어 보았다.
  
  ```
  FIRST_APP /
  		manage.py: 서버 돌릴 때 이용. 다른 기능들은 거의 만지지 않을 예정
  		db.sqlite3
  		first_app /
  				__init__
  				settings.py: 장고 app의 모든 설정들이 들어가 있음
  				urls.py: 가장 많이 쓰게 될 것. `문지기`역할. 첫 번쨰 앱의 url 설정
  				wsgi.py: 지금 말고 나중에 사용할 것.
  		..
  		..
  		(나중에 여기에 여러 app기능들을 추가해 줄 것임)
  ```

    - `manage.py`: 건드릴 일 거의 없음. 스크립트 돌릴 때만 쓸 것
    - `settings.py`: 장고 app 의 모든 설정들이 들어가 있다
    - `urls.py`: 가장 많이 쓰게 될 것. 첫 번째 앱을 만들고 url 설정을 할 때...(앞에서 설명한 `문지기` 역할의 파일)
    ```python
    @app.route(url) ==> url.py가 대신 역할을 하게 된다.
    def index():
    ```



### 장고의 컨벤션을 대략 익혔으면 직접 다뤄볼 app을 project 내부에 만들어보자
```bash
$ python manage.py startapp [pages]: 간단한 싱글페이지들이 묶여있는 app
```

  - Git Bash에서 위 명령어를 실행하면, `pages`라는 이름을 갖는 app(폴더)이 생기고 폴더 안에 여러 파일들이 생긴다. 

      - `__init__`: 페이지 관리 지점 정의

      - `model.py`: MTV 중 Model을 담당하는 곳

      - `view.py`: MTV 중 View를 담당하는 곳

      - `test.py`: 지금은 사용 안 함

        

- `settings.py`

  - `startsproject`로 만든 `first_app` 폴더 안에 있다.
  - `settings.py`에 들어가 보면 `INSTALLED_APPS`가 보이는데, 여기에 내가 만든 앱인 pages를 추가하자.
    
    ```python
    INSTALLED_APPS = [
        'pages',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

- 문지기(`url.py`): 

  - `startproject`로 만든 `first_app` 폴더 안에 있다.

  - 여기에 path를 등록한다. `경로 설정`

  - localhost:8000/ 뒤에 붙을 경로들

  - path(첫 번째 인자, 두 번째 인자): 첫 번째 인자는 경로, 두 번째 인자는 그 경로가 있는 위치

    ```python
    from django.contrib import admin
    from django.urls import path
    ```
    
    ```python
      # 이거도 써줘야 함. 내가 만든 pages라는 패키지로부터(from) views 모듈을 쓸 것이기 때문에.
      from pages import views
    ```
  
    ```python
    urlpatterns = [
        # path(첫 번째 인자: 주문서(url 경로), 두 번째 인자: view 함수의 위치)
        path('admin/', admin.site.urls),
        path('index/', views.index),    
    ]
    
    # trailing comma를 붙이는 것도 장고의 컨벤션 중 하나이다.
    # 나중에 추가될 경로가 생길 때 혹시나 comma가 없어서 생기는 오류를 방지
    # views에 있는 index 메서드를 사용할 것이라는 의미 => views.py에 index 함수를 만들어주자.
    ```


- `F1`누르고, `python interpreter` 입력. `venv`환경(python 3.7 이상)에서만 해주자!

- `views.py`:
  
  ```python
  from django.shortcuts import render
  
  # Create your views here.
  def index(request):
      # Flask에서는 render_template('index.html')
      # request 인자에는 사용자가 보낸 요청에 대한 정보가 다 들어있음
      return render(request, 'index.html')
  ```
  - `pages`에 있다.
  
  - view는 HttpResponse 객체를 return한다.
  
  - 메서드: views 모듈 안에 `def`로 만들어진 여러 함수들
    
  - render의 결과물은 뭐다? 
  
    - render 함수의 return은 HttpResponse. html 파일에 파이썬에서 다룬 변수를 넘겨주는 것이다.
    - 장고가 render(request, 'index.html')를 통해 html 타입으로 만들어 주는 것.
  
    - Django에서는 render의 첫 번째 인자로 무조건 request를 받고,
    - 두 번째 인자로는 변수를 넘겨줄 html파일을 지정해준다.
    - 이 html 파일은 `views.py`와 동일 폴더 내에 있는 `templates`폴더에 있는 html 파일을 우선 탐색한다.
    - pages > templates > index.html 만들어 주기
  
- 장고는 플라스크에서처럼 서버를 껐다 다시 켜지 않아도 새로고침만 하면 내가 요청한 페이지를 보여준다.

  

- 한 번 더!

  - `urls.py` 에서 경로 설정

    ```python
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
        path('home/', views.home),
    ]
    ```

    

  - `view.py`에서 함수 설정

    - 장고는 HttpResponse 객체를 이용해 페이지의 내용을 직접 전달해 줄 수도 있다.
    - 그런데 굳이 이렇게 할 필요는 없다. 뭐하러 이렇게 귀찮게 하나?
    
      ```python
      from django.shortcuts import render
      from django.http import HttpResponse
    
      def home(request):
          return HttpResponse(<h1>홈페이지<h1>)
      ```



# django_day_01_오후 수업

## Django 프로젝트 시작해보기 2

### Django가 data를 넘겨받는 법

- django.shortcuts로부터 render를 import하면 render는 HttpResponse 객체를 반환
- render의 context argument를 dictionary 형식으로 입력 (**Django의 컨벤션**)
- context dictionary의 `key`는 html에서 쓰일 이름, `value`는 파이썬에서 선언한 변수이다.

    ```python
    def home(request):
        return HttpResponse(
            '<!DOCTYPE><html><head></head><body>....홈페이지</body></html>'
        )
    # 이렇게 해도 가능 but 이런 짓 하지마...
    # 가능하다 != 사용한다
    ````
    ````python
    def home(request):
        name = 'Kahn'
        data = ['강동주', '김지수', '정의진']
        context = {
            # html로 보낼이름 : python에서 선언한 변수
            'name': name,
            'data': data,
        }
        return render(request, 'home.html', context)
    ```
    ```html
    <!--home.html 파일-->
    
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
      </head>
      <body>
        <h1>데이터를 넘겨받는 법</h1>
        <p> {{ name }}</p>
        {% for item in data %}
          <p>{{item}}</p>
        {% endfor %}
      </body>
    </html>
    ```

- 개꿀팁쓰!!!!!!

  - `Ctrl+p`로 검색하여 `대충` `비슷`하게 매칭되는 파일로 이동하자
  - 언제까지 마우스로 찾아다닐꺼야~~

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
      .numbers {
        margin-left: 32px;
      }
    
    </style>
  </head>
  <body>
    <h1>이것은 로또번호다</h1>
    <!-- {{ lotto }} -->
    <p>[</p>
    {% for number in lotto %}
      <p class="numbers">{{ number }},</p>
    {% endfor %}
    <p>]</p>
  </body>
  </html>
  ```

- ```python
  def lotto(request):
      import random
      mylotto = random.sample(range(1,46),6)
      context = {
          'lotto':mylotto
      }
      return render(request, 'lotto.html', context)
  ```

- ```python
  urlpatterns = [
      path('lotto/', views.lotto),
  ]
  ```

- 로또 홈페이지처럼, 로또 번호를 색깔이 들어간 원 배경에 담아보자.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
      p {
        margin: 0;
      }
      .box {
        display: flex;
        justify-content: start;
      }
      .ball {
        margin: 10px;
        height: 30px;
        width: 30px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-content: center;
      }
      .b1 {
        border: 1px solid gold;
        background-color: gold;
      }
      .b2 {
        border: 1px solid orangered;
        background-color: orangered;
      }
      .b3 {
        border: 1px solid cornflowerblue;
        background-color: cornflowerblue;
      }
      .b4 {
        border: 1px solid seagreen;
        background-color: seagreen;
      }
      .b5 {
        border: 1px solid yellowgreen;
        background-color: yellowgreen;
      }
      .numbers {
        line-height: 30px;
        color: white;
      }
    
    </style>
  </head>
  <body>
    <h1>이번주 토요일엔 로또 당첨돼서 <span style="color:red">싸피</span> 탈주 하즈아~</h1>
    <h1>{{ lotto }}</h1>
  
    <div class="box">
        {% for number in lotto %}
          {% if number > 40 %}
            <div class="ball b5">
              <p class="numbers">{{ number }}</p>
            </div>
          {% elif number > 30 %}
            <div class="ball b4">
              <p class="numbers">{{ number }}</p>
            </div>
          {% elif number > 20 %}
            <div class="ball b3">
              <p class="numbers">{{ number }}</p>
            </div>
          {% elif number > 10 %}
            <div class="ball b2">
              <p class="numbers">{{ number }}</p>
            </div>
          {% else %}
            <div class="ball b1">
              <p class="numbers">{{ number }}</p>
            </div>
          {% endif %}
        {% endfor %}
      </div>
  </body>
  </html>
  ```

  

### DTL
- Django Template Language 관련 문법

- python과 유사할 뿐 python이 아니다!
  
- 공식 문서:  **https://docs.djangoproject.com/en/2.2/ref/templates/language/**
  
  - for
    ```html
      <h2>for문 활용법</h2>
      <!-- <h2>데이터가 없을 때는 empty 부분이 실행된다.</h2> -->
    
      {% for movie in empty_data %}
      <!--forloop.counter는 번호를 매김. python enumerate처럼-->
      <p>{{ forloop.counter }} : {{ movie }}</p>
      {% empty %}
      <p>영화 데이터가 없습니다.</p>
    
      {% endfor %}
    ```
  - 이중 for문
    ```html
      <h2>이중 for문</h2>
      {% for array in matrix %}
      	{% for num in array %}
      		<p>{{ num }}</p>
      	{% endfor %}
      {% endfor %}
    ```
  ```
  
  - if
    ```html
      <h1>DTL 조건문</h1>
      {% if number > 0 %}
      <p>이건 0보다 큰 숫자야</p>
      {% endif %}
  ```
  
- helper / filter
  
    ```html
      <h2>다양한 helper / filter</h2>
      <h3>helper</h3>
      <!--Displays random “lorem ipsum” Latin text. This is useful for providing sample data in 	templates.-->
      {% lorem 3 p random %}
    
      <h3>filter</h3>
      {% for movie in empty_data %}
        {{ movie|length }}
        <!-- movie에 들어간 영화 제목의 길이를 출력-->
        {{ movie|truncatechars:3 }}
        <!-- movie에 들어간 영화 제목의 길이를 3(세자리)까지만 표시-->
      {% endfor %}
  ```
  
- datetime
  
    ```html
      <h4>datetime</h4>
      {% now 'Y년 M월 m월 d일 h시 i분 a day' %}
  ```
  
  - `setting.py`에서 시간 설정 가능('Asia/Seoul') 기본 설정은 `UTC`



### Dynamic Web(동적 웹)
- 사용자가 입력한 값마다 다른 결과의 웹 페이지를 보여준다.

- urls.py에 아래 코드를 추가해보자
  ```python
  path('cube/<num>/', views.cube), # num 데이터를 받는다. 그러나 이건 string임
  path('cube/<int:num>', views.cube) # string을 int로 받기 위해서 해줘야하는 작업
  ```
  
#### GET method 사용하기
  ```python
def match(request):
    import random
    goonghap = random.randint(50,100)
    me = request.POST.get('me')
    you = request.POST.get('you')
    test = request.path_info
    context = {
        'goonghap': goonghap,
        'me': me,
        'you': you,
        'test': test,
    }
    return render(request, 'match.html', context)
  ```
  ```python
print(request)
print(request.GET)
print(request.GET.get('me'))
  ```
  ```python
  >>> <WSGIRequest: GET '/match/?me=a&you=b'>
  >>> <QueryDict: {
        'goonghap': goonghap,
        'me': me,
        'you': you,
        'test': test,
      }>
  >>> me
  ```




#### POST method 사용하기
- csrf: cross-site reference) 추가
- POST 방식으로 사용자의 데이터를 받을 때, csrf_token을 함께 보내도록 한다.
  ```python
  print(request)
  print(request.POST)
  print(request.POST.get('me'))
  ```
  ```python
  >>> <WSGIRequest: POST '/match/'>
  >>> <QueryDict: {
          'csrfmiddlewaretoken': ['---some token---'],
          'goonghap': goonghap,
          'me': me,
          'you': you,
          'test': test,
          }>
  >>> me
  ```
  ```html
  <body>
    <h1>안녕하세요</h1>
    <form action="/match/" method="POST"> <!--디폴트는 GET-->
      {% csrf_token %}
      당신의 이름: <input type="text" name="me">
      당신이 좋아하는 분의 이름: <input type="text" name="you">
      <input type="submit"></input>
    </form>
  </body>
  ```

  

- 오늘 했던 것들: `url.py`

  ```python
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index),
      path('home/', views.home),
      path('lotto/', views.lotto),
      path('cube/<int:num>/', views.cube),
      # num은 str로 들어가니까, int로 형 변환을 해줘야 한다.
      path('match/', views.match),
  ]
  ```

  ```python
  from django.shortcuts import render
  from django.http import HttpResponse
  
  
  # Create your views here.
  def index(request):
      return render(request,'index.html')
  
  def home(request):
      # return HttpResponse('<!DOCTYPE><html>....홈페이지')
      name = 'Kahn'
      data = ['강동주', '김지수', '정의진']
      empty_data = ['엄복동', '클레멘타인', '성냥팔이소녀의 재림']
      matrix = [[1,2,3],[4,5,6]]
      context = {
          'name': name,
          'data': data,
          'empty_data': empty_data,
          'matrix': matrix,
          'number': 10,
      }
      return render(request, 'home.html', context)
  
  def lotto(request):
      import random
      mylotto = sorted(random.sample(range(1,46),6))
      context = {
          'lotto':mylotto,
          'number': 10,
      }
      return render(request, 'lotto.html', context)
  
  def cube(request, num):
      result = num ** 3
      context = {
          'result': result,
      }
      return render(request, 'cube.html', context)
  
  def match(request):
      import random
      goonghap = random.randint(50,100)
      me = request.POST.get('me')
      you = request.POST.get('you')
      test = request.path_info
      context = {
          'goonghap': goonghap,
          'me': me,
          'you': you,
          'test': test,
      }
      return render(request, 'match.html', context)
  ```
