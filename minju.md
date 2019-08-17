\Django
### 장단점
장: 독선적이어서 유지보수가 쉽다, 웹서비스를 편하게 만들 수 있게 제공한다
### 웹서비스
요청과 응답이 존재,
### MVC  모델
model view controller
model = 데이터베이스(저장만)
컨트롤러 = 작업공간
뷰 = 보여주는 곳
<img src = "https://danielmiessler.com/images/MVC1.png" width = 500px>

### MTV 모델
template = view, 화면
model = 컨트롤러, 데이터베이스에서 탐색 작업 함
view = 중간관리자, 특정 관리자 수행(사용자가 인풋을 보내면 모델에 요청함 , 함수 덩어리)
## 가상환경
설정하는 이유: 프로젝트 하나 당 가상환경 하나씩-프로젝트마다 사용하는 라이브러리, 그 버전이 다를 수 있다
그에 대한 호환성, 의존성이 발생
```bash
$ python -V  # 파이썬 버전 확인, 3.7인지 확인
Python 3.7.4
(3.7.4)  
$ python -m venv venv  # 폴더 만들기
$ source venv/Scripts/activate  # 가상환경 적용하기
$ pip list  # 설치된 모듈 확인(깨끗한가)
```
### 가상환경 자동 설정하기 (vscode 설정)
파이썬, 장고 extension 설치
ctrl shift p - python select interpreter - 가상환경 설정(.venv/Scripts/python.exe)
vscode/setting.json파일이 생성되며 터미널에서 자동으로 가상환경이 적용되면 굿
[Git Ignore] - gitignore.io
```bash
$ touch .gitignore
# 그 파일에 복붙
```
### vscode django 환경세팅
settings.json 설정하기
```json
{
    // 파이썬 환경 선택
    "python.pythonPath": "venv\\Scripts\\python.exe",
    // 장고에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements",
    },
    // 장고 html에서도 html emet을 적용
    "emmet.includeLanguages": {"django-html": "html"},
    // 장고 html에서 tab size를 2칸으로 적용
    "[django-html]" : {
        "editor.tabsize":2,
    },
}
```
드디어 장고 설치
```bash
$ pip install django
```
## VIEW.PY
MTV모델을 따른다. model(데이터베이스), template(사용자에게 보여지는 페이지), view(작업을 하는 공간)
url과 view가 연결되어 보여지게 된다. 
### 파이썬 파일  삼대장
1. models.py : 데이터베이스 관리
2. view.py : 사용자에게 보여지는 로직 담당, view함수 정의 및 작업 명시
3. urls.py : 사용자가 들어올 수 있는 경로 설정
---
## START DJANGO PROJECT
가상환경에서 실행 
장고를 설정한 순간부터 django.admin이라는 command를 사용 가능. 이를 통해 장고 프로젝트에 여러가지 명령을 할 수 잇다
### 프로젝트 시작
```bash
$ django-admin startproject Django_intro .
$ python manage.py runserver  # 드디어 사이트 표시됨 127.0.0.1 로컬호스트 8000번 포트로 간다
```
현재 디렉토리에서 django_intro라는 이름으로 프로젝트 시작
네이밍: _는 사용 불가, 파이썬과 장고에서 이미 사용되는 이름은 사용하지 않는다
## 셋팅 설정
```python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```
## <시작>
https://docs.djangoproject.com/en/2.2/intro/tutorial01/
### 프로젝트 VS 앱
프로젝트와 앱은 무엇이 다를까요? 앱은 특정한 기능(블로그나 공공 기록물을 위한 데이터베이스나, 간단한 설문조사 앱)을 수행하는 웹 어플리케이션을 말합니다. 프로젝트는 이런 특정 웹 사이트를 위한 앱들과 각 설정들을 한데 묶어놓은 것입니다. 프로젝트는 다수의 앱을 포함할 수 있고, 앱은 다수의 프로젝트에 포함될 수 있습니다.
어플 - 로직 수행
프로젝트 - 어플 모으기
## settings.json
```json
    // 장고 html에서도 html emet을 적용
    "emmet.includeLanguages": {"django-html": "html"},
    // 장고 html에서 tab size를 2칸으로 적용
    "[django-html]" : {
        "editor.tabsize":2,
    },
```
## pages라는 앱 만들고 시작
```bash
# 앱 만들기
$ python manage.py startapp 이름
```
### 장고 프로젝트에게 어플리케이션 만들었다고 알리기
setting.py 에서
```python
# Application definition
INSTALLED_APPS = [
    #local apps(내가 만든 앱)
    'pages', # 여기에 어플리케이션 이름 넣기
    # third party apps(pip로 깔은 것들 bootstrap)
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',] 
```
## [ 어플리케이션 내 페이지 만들기 ]
### 1) URL만들기
url.py에서 path 만들어서 사용자가 이동할 곳 만들어주기
```python
from pages import views
# 어디로 들어간 이후 로그인 페이지 관련 함수로 이동하라는 명령
urlpatterns = [
    path('index/',views.index), 
    
    path('admin/', admin.site.urls),
    # paht('login/', 로그인 페이지관련 함수)
]
```
### 2) VIEW에서 함수 작성하기
pages 앱 내 view.py 에서 정의해 url과 1:1 맵핑한다
views.index가 실행된다 - 실행되면 index.html이 실행됨
```python
def index(request):        # 첫 번째 인자는 반드시 request가 온다, 사용자가 보내는 요청 정보가 있다
    return render(request, 'index.html')  # 첫 번째 인자는 반드시 request가 온다, 어떤 페이지 이름을 보여줄 것인지 이름 짓기
```
### 3) html 파일 만들기
해당 어플리케이션 파일 - templates - index.html 파일 만들기
## Template Variable 이용
```python
# urls.py
path('times/<int:num1>,<int:num2>',views.times)  # <str:name>도 가능
# views.py
def times(request, num1, num2):
    context = {'gop': num1 * num2, 'num1' : num1, 'num2' : num2}
    return render(request, 'times.html',context)
# times.html
# <p>둘의 곱은 {{ gop }} 둘은 각각 {{ num1 }}, {{ num2 }} </p>
```
기타 다른 것(이미지, 랜덤 뽑기 이용)
```python
def image(request):
    context = {'image':'https://picsum.photos/500'}
    return render(request, 'image.html',context)
# html : <img src="{{ image }}" alt="">
def dinner(request, name):
    menu = ['양자강','빨강통닭','파란불고기']
    pick = random.choice(menu)
    context = {'pick': pick}
    context = {'name': name}
    return render(request, 'dinner.html',context)
```