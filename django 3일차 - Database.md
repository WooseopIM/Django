# 190819

## Django 리뷰

- 지난주에 했던 것을 기반으로 오늘 새로운 프로젝트를 시작해보자

- 프로젝트 이름은 BLOG, 앱 이름은 articles로 하자

- ```bash
  $ venv	# 가상환경 시작하자! 꼭! 까먹지 말고!
  $ mkdir BLOG
  $ django-admin startproject blog BLOG
  $ python manage.py runserver	# 로켓 모습 보이면 완료된 것!
  $ python manage.py startapp articles
  ```

- 



## Database 기초

스키마: 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

SQL: Structured Query Language

관계형 데이터베이스 관리 시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

ORM:Create Read Update Delete 반드시 쓰게 될 것. 네이버 카카오 단골 면접 질문

```bash
$ python manage.py makemigrations
Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Article
```

model.py를 보고, migrations 파일을 만들어줌. 설계도를 만드는 과정.

명령어를 하나 더 쳐보자.

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying articles.0001_initial... OK # 내가 직접 만든 것은 articles가 유일.
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```

```bash
$ python mange.py makemigrations
You are trying to add a non-nullable field 'image_url' to article without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> ''
Migrations for 'articles':
  articles\migrations\0002_article_image_url.py
    - Add field image_url to article
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying articles.0002_article_image_url... OK
(3.7.3)

$ python manage.py sqlmigrate articles 0001
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" text NOT NULL, "contents" text NOT NULL, "created_at" datetime NOT NULL);
COMMIT;

$ python manage.py shell
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

```

DB를 파이썬 코드로 조작하자.

```shell
>>> from articles.models import Article
>>> Article.objects.all()
<QuerySet []>
>>> article.title = "이건 제목"
>>> article.content = "이건 내용"
>>> Article.objects.all()
<QuerySet []>
>>> article.save() # 저장을 하면 앞으로도 조회가 계속 가능하게 됨.ㅇ
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>]>
>>> len(Article.objects.all())
1
>>> Article.objects.all()[0]
<Article: Article object (1)>
>>> dir(Article.objects.all())
['__and__', '__bool__', '__class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_hints', '_batched_insert', '_chain', '_clone', '_combinator_query', '_create_object_from_params', '_db', '_earliest', '_extract_model_params', '_fetch_all', '_fields', '_filter_or_exclude', '_for_write', '_has_filters', '_hints', '_insert', '_iterable_class', '_iterator', '_known_related_objects', '_merge_known_related_objects', '_merge_sanity_check', '_next_is_sticky', '_populate_pk_values', '_prefetch_done', '_prefetch_related_lookups', '_prefetch_related_objects', '_raw_delete', '_result_cache', '_sticky_filter', '_update', '_validate_values_are_expressions', '_values', 'aggregate', 'all', 'annotate', 'as_manager', 'bulk_create', 'bulk_update', 'complex_filter', 'count', 'create', 'dates', 'datetimes', 'db', 'defer', 'delete', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'get', 'get_or_create', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'none', 'only', 'order_by', 'ordered', 'prefetch_related', 'query', 'raw', 'resolve_expression', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'using', 'values', 'values_list']

```

```bash
$ python manage.py createsuperuser
```

