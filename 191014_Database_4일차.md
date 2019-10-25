# 190923 Database 1일차

## Database

- 체계화된 데이터의 모임
- 여러 사람이 공유/사용할 목적으로 통합 관리되는 정보의 집합
- 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜놓은 자료의 집합체

```bash
$ python manage.py shell_plus
```
```shell
# 가장 최근에 만든 crud 프로젝트에서
>>> qs = Post.objects.all()

>>> qs[0]
<Post: Post object (3)>

>>> qs.query
<django.db.models.sql.query.Query object at 메모리상 주소>

>>> print(qs.query)
SELECT "posts_post"."id", "posts_post"."title", "posts_post"."content", "posts_post"."image", "posts_post"."created_at", "posts_post"."updated_at" FROM "posts_post" ORDER BY "posts_post"."id" DESC

```

- csv, 텍스트 등 파일로 데이터들을 정리할 수 있는데 새로운 언어를 하나 배워야 쓸 수 있는 DB를 쓰는 이유?

## 데이터 베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결정(정확한 정보 보장)
- 데이터 일관성
- 데이터 독립성(물리적 독립성, 논리적 독립성)
- 데이터 표준화
- 데이터 보안 유지
- 다 필요 없고 그냥 편하게 데이터를 관리할 수 있음



## RDBMS(관계형 데이터베이스 관리 시스템)

- 관계형 모델을 기반으로 하는 DB 관리 시스템
- 대표적 오픈소스 RDBMS(MySQL, SQLite, PostgreSQL)
- ORACLE
- Microsoft SQL Server
- 관계를 표현한다: 행의 무의미한 데이터를 특정 의미를 갖도록 column으로 속성을 부여해줌



## 스키마(Schema)

- 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
- 표를 통해서 구현. Meta Data.
- PK(기본키): 각 행(레코드)의 고유값. 반드시 설정하여야 하며 장고 같은 경우에서는 안 해도 알아서 만들어준다. 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.



## SQL

- Structured Query Language
- DB를 다룰 때 가장 표준이 되는 언어
- RDBMS의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
- 자료 검색, 자료 관리, 스키마 생성 및 수정, DB 객체 접근 조정 관리 등
- 블록체인에서 쓰려는 움직임도 있음
- DDL(데이터 정의 언어)
- DML(데이터 조작 언어)  - INSERT, DELETE, UPDATE, SELETE 
- DCL(데이터 제어 언어) - SSAFY에서는 거의 안 배울 것



## 직접 다뤄보자. Table과 DB

- https://www.sqlite.org/index.html

- Precompiled Binaries for Windows

  ```
  sqlite-dll-win64-x64-3290000.zip
  (788.61 KiB)		64-bit DLL (x64) for SQLite version 3.29.0.
  (sha1: c88204328d6ee3ff49ca0d58cbbee05243172c3a)
  
  
  sqlite-tools-win32-x86-3290000.zip
  (1.71 MiB)		A bundle of command-line tools for managing SQLite database files, including the command-line shell program, the sqldiff.exe program, and the sqlite3_analyzer.exe program.
  (sha1: f009ff42b8c22886675005e3e57c94d62bca12b3)
  ```

- ```bash
  $ cd ~
  $ mkdir sqlite
  # 다운 받은 프로그램 파일들을 sqlite 폴더에 옮겨주자
  ```

- 환경변수에 저장

  - sqlite3.exe의 속성에서 위치(경로)를 복사
  - 내PC 우클릭, 고급시스템설정, 환경변수
  - `student에 대한 사용자 변수의 Path`에 경로 새로 만들기(시스템 변수에 만들어주는 건 너무 헤비해...)
  - 복사한 경로를 붙여넣어준다.
  - 이제 installer가 없어도 걱정하지 말자

- 시그윈, winpty: git bash가 알게 모르게 쓰고 있는 것들. bash를 통해 sqlite3를 쓰고 싶으면 아래와 같이 해준다.

- ```bash
  $ winpty sqlite3
  SQLite version 3.29.0 2019-07-10 17:32:03
  Enter ".help" for usage hints.
  Connected to a transient in-memory database.
  Use ".open FILENAME" to reopen on a persistent database.
  sqlite> .exit
  
  student@M701 MINGW64 ~
  $ 
  ```

- 줄여주자

  ```bash
  $ cd ~
  $ code .bashrc
  ```

  ```python
  alias sqlite3='winpty sqlite3'
  ```

  ```bash
  $ source ~/.bashrc
  $ sqlite3
  SQLite version 3.29.0 2019-07-10 17:32:03
  Enter ".help" for usage hints.
  Connected to a transient in-memory database.
  Use ".open FILENAME" to reopen on a persistent database.
  sqlite> .exit
  
  student@M701 MINGW64 ~
  $ 
  ```

- crud 프로젝트에서 sqlite3 사용하기

- DB를 다루는 커맨드를 입력할 때는 `.`으로 시작한다.

  ```bash
  $ sqlite3 db.sqlite3
  SQLite version 3.29.0 2019-07-10 17:32:03
  Enter ".help" for usage hints.
  sqlite> .databases
  ```

- `.databases`: 현재 db가 있는 곳의 경로를 보여준다.

- `.tables`: 현재 db가 갖고 있는 table을 보여준다.
  app이름_model이름

- `SELECT * FROM posts_post;`: posts에 있는 모든 글을 보여준다.

- `SELECT title FROM posts_post;`: posts에 있는 글의 제목을 보여준다.

- bash 인코딩 바꿔주기: options > Text > Character set을 UTF-8로 설정



## 실습

- ```bash
  $ cd ~
  $ mkdir database
  $ mv ~/Downloads/hellodb.csv .
  $ mv ~/Downloads/users.csv .
  ```

- Database 생성:

  ```bash
  $ sqlite3 database
  ```

  해당 데이터베이스 파일이 있으면 해당 DB를 콘솔로 연다.

  없으면 파일을 새로 생성하고 해당 DB를 콘솔로 연다.

- ```bash
  $ sqlite3 tutorial.sqlite3
  SQLite version 3.29.0 2019-07-10 17:32:03
  Enter ".help" for usage hints.
  sqlite> .databases
  main: C:\Users\student\codes\db\tutorial.sqlite3
  sqlite> ^Z
  
  $ ls
  hellodb.csv  tutorial.sqlite3  users.csv
  ```

  `tutorial.sqlite3`라는 데이터베이스 파일을 만들어준다.

- `.mode csv`: 아가리 벌려, csv 들어간다

- `.import hellodb.csv examples`: hellodb.csv 파일을 examples에 넣어줘

- `.headers on`: 헤더를 단 상태로 나온다.

- `.mode column`: 엑셀 느낌처럼 콘솔창에 보이게 된다.

  ```sqlite
  sqlite> SELECT * FROM examples;
  1,"길동","홍",600,"충청도",010-2424-1232
  sqlite> .headers on
  sqlite> SELECT * FROM examples;
  id,first_name,last_name,age,country,phone
  1,"길동","홍",600,"충청도",010-2424-1232
  sqlite> .mode column
  sqlite> SELECT * FROM examples;
  id          first_name  last_name   age         country     phone
  ----------  ----------  ----------  ----------  ----------  -------------
  1           길동          홍           600         충청도         010-2424-1232
  sqlite>
  
  ```

- TABLE 생성해보기

  ```sqlite
  sqlite> CREATE TABLE classmates (
      id INTEGER PRIMARY KEY,
      name TEXT);
  sqlite> .tables
  classmates examples
  ```

  하나의 DB는 여러 개의 TABLE을 가질 수 있다.

- SQLite는 동적 데이터 타입으로, 기본적으로 유연하게 데이터가 들어간다. 

- 제일 많이 쓰이는 Datatype: INTEGER(숫자), TEXT(글자)

- `.schema classmates`: classmates table을 볼 수 있다.

- `.schema examples`: examplesdml  table을 볼 수 있다.

- `DROP TABLE examples;`: example table을 지운다.

- `DROP TABLE classmates;`: classmates table을 지운다.

- 이 상태에서 `.tables`를 치면 아무것도 뜨지 않는다. (다 지웠기 때문)

- 새로 classmates table 만들어보기

  ```sqlite
  sqlite> .schema classmates
  CREATE TABLE classmates (id INTEGER PRIMARY KEY, name TEXT);
  
  sqlite> DROP TABLE examples;
  
  sqlite> DROP TABLE classmates;
  
  sqlite> .tables
  
  sqlite> CREATE TABLE classmates (
     ...> name TEXT,
     ...> age INTEGER,
     ...> address TEXT);
     
  sqlite> .schema classmates
  CREATE TABLE classmates (
  name TEXT,
  age INTEGER,
  address TEXT);
  
  ```

## Data 추가(INSERT)

- 특정 테이블에 새로운 행을 추가하여 데이터를 추가할 수 있다.

- classmates 테이블에 이름이 홍길동이고 나이가 23인 데이터를 넣어보자.

- ```sqlite
  sqlite> INSERT INTO classmates (name, age) VALUES ('홍길동',23);
  
  sqlite> SELECT * FROM classmates;
  name        age         address
  ----------  ----------  ----------
  홍길동         23
  
  ```

- 이름만 넣는 것도 가능할까?

  ```sqlite
  sqlite> INSERT INTO classmates (name) VALUES ('김싸피');
  
  sqlite> SELECT * FROM classmates;
  name        age         address
  ----------  ----------  ----------
  홍길동         23
  김싸피
  
  ```

- 3개를 다 넣어보자

  ```sqlite
  sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍길동',30,'서울');
  
  sqlite> SELECT * FROM classmates;
  name        age         address
  ----------  ----------  ----------
  홍길동         23
  김싸피
  홍길동         30          서울
  
  ```

- 현재 존재하는 칼럼 3개에 값을 다 넣을거면 바로 VALUES를 넣어도 된다.

  ```sqlite
  sqlite> INSERT INTO classmates VALUES ('이삼성',50,'수원');
  
  sqlite> SELECT * FROM classmates;
  name        age         address
  ----------  ----------  ----------
  홍길동         23
  김싸피
  홍길동         30          서울
  이삼성         50          수원
  
  ```

- 이런 방법으로는 똑같은 속성을 가진 데이터를 INSERT 하더라도 똑같은 값이 계속 들어가게 된다.

  ```sqlite
  # 한번 더 하게 되면?
  sqlite> INSERT INTO classmates VALUES ('이삼성',50,'수원');
  
  sqlite> SELECT * FROM classmates;
  name        age         address
  ----------  ----------  ----------
  홍길동         23
  김싸피
  홍길동         30          서울
  이삼성         50          수원
  이삼성			50			수원
  ```

- address 값이 없는 상태로 저장되는게 맞나? `NO!`
  주소가 꼭 필요한 정보라면 공백으로 비워두면 안된다(`NOT NULL: 공백을 허용하지 않는다. 공백으로 놔둔 속성이 있으면 어떻게 될까?`)
  Default 값을 두거나, NOT NULL로 설정을 해주거나.

- Table 다시 만들기 (DROP먼저하고 schema를 타이트하게 짜보자)

  PRIMARY KEY는 INTEGER만 사용 가능하다

  ```sqlite
  sqlite> DROP TABLE classmates;
  sqlite> CREATE TABLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT NOT NULL,
     ...> age INTEGER NOT NULL,
     ...> address TEXT NOT NULL
     ...> );
     
  sqlite> .tables
  classmates
  
  sqlite> INSERT INTO classmates VALUES ('김싸피',30,'서울');
  Error: table classmates has 4 columns but 3 values were supplied
  
  sqlite> INSERT INTO classmates VALUES (1, '김싸피',30,'서울');
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  
  sqlite> INSERT INTO classmates VALUES (1, '이삼성', 50, '수원');
  Error: UNIQUE constraint failed: classmates.id
  
  sqlite> INSERT INTO classmates VALUES (5, '이삼성', 50, '수원');
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  5           이삼성         50          수원
  
  sqlite> INSERT INTO classmates (name, age, address) VALUES ('조동빈',28,'서울');
  sqlite> SELECT * FROM classmates
     ...> ;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  5           이삼성         50          수원
  6           조동빈         28          서울
  
  sqlite> INSERT INTO classmates VALUES (4, '오재석',27,'구미');
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  4           오재석         27          구미
  5           이삼성         50          수원
  6           조동빈         28          서울
  
  sqlite> INSERT INTO classmates (name, age, address) VALUES ('이한얼',27,'서울');
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  4           오재석         27          구미
  5           이삼성         50          수원
  6           조동빈         28          서울
  7           이한얼         27          서울
  
  sqlite> INSERT INTO classmates (age, address) VALUES (30, '부산');
  Error: NOT NULL constraint failed: classmates.name
  sqlite>
  
  
  ```

- PK 컬럼은 직접 작성하기보다 SQLite가 만들어주는 rowid를 사용하는 것이 좋다(나중에 가면 rowid의 불편함도 겪게 될 것)

- 그렇다면 장고는 어떻게 PK컬럼을 다룰까?
  가장 최근에 만든 장고 crud 프로젝트에서 `.schema posts_post`로 확인해보자

  ```sqlite
  sqlite> .schema posts_post
  CREATE TABLE IF NOT EXISTS "posts_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content"
   text NOT NULL, "image" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
  
  sqlite>
  
  ```


## Date 조회(SELECT)

- 특정한 table에서 원하는 개수만큼 column 가져오기, `LIMIT`
  데이터 수가 많으면 위에서부터 몇 개를 가져오라고 할 때 쓰인다.
  나중에는 주로 1개의 데이터를 뽑을 일이 많기 때문에 유용한 커맨드.

  ```sqlite
  sqlite> SELECT * FROM classmates LIMIT 2;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  4           오재석         27          구미
  ```

- 특정 column 값을 특정 위치에서부터 몇 개만 가져온다면?
  LIMIT과 OFFSET은 한 세트!

  ```sqlite
  sqlite> SELECT * FROM classmates LIMIT 3;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  4           오재석         27          구미
  5           이삼성         50          수원
  
  sqlite> SELECT * FROM classmates LIMIT 3 OFFSET 1;
  id          name        age         address
  ----------  ----------  ----------  ----------
  4           오재석         27          구미
  5           이삼성         50          수원
  6           조동빈         28          서울
  
  sqlite> SELECT * FROM classmates LIMIT 2 OFFSET 6;
  전체 값이 5개밖에 없으므로 OFFSET 6하면 아무것도 안뜬다.
  ```

- classmates에서 id, name column 값을 세 번째에 있는 값 하나만 가져오면?

  ```sqlite
  sqlite> SELECT * FROM classmates LIMIT 1 OFFSET 2;
  id          name        age         address
  ----------  ----------  ----------  ----------
  5           이삼성         50          수원
  
  ```

- 파이썬에서 사용하던 `Post.objects.get(pk=1)`을 sql문으로 써보면 어떻게 나오나?

  ```sqlite
  sqlite> SELECT * FROM classmates WHERE id=1;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  sqlite> SELECT * FROM classmates WHERE name='김싸피';
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  
  ```

  내가 만든 파일에서는 아래와 같이 나온다(Character set)을 다시 eucKR로 바꿔줘야 값이 보인다. 완전 일치하는 항목에 대해서만 가능(부분 검색은 불가능, 부분 검색이 가능하게 하는 것도 배울 예정)

  ```shell
  >>> p1 = Post.objects.get(pk=1)
  >>> p1.title
  >>> p1.title
  '벤틀리 너무 귀여워'
  >>> Post.objects.get(title='벤틀리 너무 귀여워')
  >>> <Post: Post object (1)>
  >>> Post.objects.get(title='벤틀리')
  DoesNotExist
  
  근데 내 꺼에서는 아래 에러메시지가 뜬다
  posts.models.Post.MultipleObjectsReturned: get() returned more than one Post -- it returned 2!
  ```

  ```sqlite
  sqlite> SELECT * FROM classmates WHERE address='서울';
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  6           조동빈         28          서울
  7           이한얼         27          서울
  ```


- classmates에서 age 값 전체를 중복 없이 가져온다면?

  ```sqlite
  sqlite> SELECT age FROM classmates;
  age
  ----------
  30
  27
  50
  28
  27
  
  
  sqlite> SELECT DISTINCT age FROM classmates;
  age
  ----------
  30
  27
  50
  28
  
  ```

- 마찬가지로 classmates에서 address 값 전체를 중복 없이 가져올 수도 있다

  ```sqlite
  sqlite> SELECT DISTINCT address FROM classmates;
  address
  ----------
  서울
  구미
  수원
  ```

## Data 삭제(DELETE)
- 특정 table에 특정한 레코드를 삭제할 수 있다.
- 검색에서 사용 했던 `WHERE`을 이용해서 삭제할 대상을 지정할 수 있다.

- 내가 만든 classmates 테이블에서 이름이 '김싸피'인 레코드를 지우고 싶으면?

  ```sqlite
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  1           김싸피         30          서울
  4           오재석         27          구미
  5           이삼성         50          수원
  6           조동빈         28          서울
  7           이한얼         27          서울
  sqlite> DELETE FROM classmates WHERE id=1;
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  4           오재석         27          구미
  5           이삼성         50          수원
  6           조동빈         28          서울
  7           이한얼         27          서울
  
  ```

- 나이가 27살인 레코드를 지우면 27살인 레코드들이 '모두' 지워지므로 데이터들을 다룰 때는 pk를 기준으로 다루자

  ```sqlite
  sqlite> SELECT * FROM classmates WHERE age=27;
  id          name        age         address
  ----------  ----------  ----------  ----------
  4           오재석         27          구미
  7           이한얼         27          서울
  
  
  sqlite> DELETE FROM classmates WHERE age=27;
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  5           이삼성         50          수원
  6           조동빈         28          서울
  
  ```

- SQLite는 기본적으로 일부 행을 삭제하고 새 행을 삽입하면 삭제 된 행의 값을 재사용하려고 시도한다.

  ```sqlite
  sqlite> DELETE FROM classmates WHERE id=6;
  sqlite> INSERT INTO classmates (name,age,address) VALUES ('임우섭',28,'부산');
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  5           이삼성         50          수원
  6           임우섭         28          부산
  sqlite> 이러면 안돼
  
  ```

  

- 이전에 삭제 된 행의 값을 재사용하지 않고 사용하지 않은 다음 행 값으로 사용하게 하려면? `AUTOINCREMENT`
  '왕건'은 자동으로 `id=3`의 값을 갖게 된다.

  ```sqlite
  sqlite> CREATE TABLE tests (
     ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
     ...> name TEXT NOT NULL
     ...> );
  sqlite> .tables
  classmates  tests
  
  sqlite> INSERT INTO tests (name) VALUES ('홍길동'),('임꺽정');
  sqlite> SELECT * FROM tests;
  id          name
  ----------  ----------
  1           홍길동
  2           임꺽정
  
  sqlite> DELETE FROM tests WHERE id=2;
  sqlite> SELECT * FROM tests;
  id          name
  ----------  ----------
  1           홍길동
  
  
  sqlite> INSERT INTO tests (name) VALUES ('왕건');
  sqlite> SELECT * FROM tests;
  id          name
  ----------  ----------
  1           홍길동
  3           왕건
  
  ```

  

- 사용자가 레코드를 지우더라도 DB에는 흔적을 남기게 된다.

## Date 수정(UPDATE)

- classmates 테이블에 id가 6인 레코드를 수정하여, 이름을 곽철용 바꿔보자

  ```sqlite
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  5           이삼성         50          수원
  6           임우섭         28          부산
  
  
  sqlite> UPDATE classmates SET name='곽철용' WHERE id=6;
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  5           이삼성         50          수원
  6           곽철용         28          부산
  
  
  sqlite> INSERT INTO classmates (name, age, address) VALUES ('고니',28,'남원');
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
  5           이삼성         50          수원
  6           곽철용         28          부산
  7           고니          28          남원
  
  
  sqlite> UPDATE classmates SET name='아귀' WHERE age=28;
  sqlite> SELECT * FROM classmates;
  id          name        age         address
  ----------  ----------  ----------  ----------
5           이삼성         50          수원
  6           아귀          28          부산
  7           아귀          28          남원
  
  ```
  
- user.csv 파일을 가지고 database > users 테이블에 데이터를 추가해보자

  ```bash
  $ sqlite3 tutorial.sqlite3
  ```

  ```sqlite
  SQLite version 3.29.0 2019-07-10 17:32:03
  Enter ".help" for usage hints.
  sqlite> .mode csv
  sqlite> .import users.csv users
  sqlite> SELECT * FROM users;
  
  자료의 1000개 레코드들이 쭈루룩 뜸
  ```

  스키마를 확인해보면 모든 컬럼들이 TEXT로 지정되어 있음

  ```sqlite
  sqlite> .schema users
  CREATE TABLE users(
    "id" TEXT,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" TEXT,
    "country" TEXT,
    "phone" TEXT,
    "balance" TEXT
  );
  ```

  새로운 table을 만들어 각 컬럼에 맞는 속성을 정해주자

  ```sqlite
  sqlite> CREATE TABLE users2 (
     ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
     ...> first_name TEXT,
     ...> last_name TEXT,
     ...> age INTEGER,
     ...> country TEXT,
     ...> phone TEXT,
     ...> balance INTEGER
     ...> );
  
  
  sqlite> .schema users2
  CREATE TABLE users2 (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT,
  last_name TEXT,
  age INTEGER,
  country TEXT,
  phone TEXT,
  balance INTEGER
  );
  
  ```

  header 행이 있기 때문에 datatype mismatch 오류가 발생한다.

  header 행이 있는지 항상 파악하고 import해주자.

  ```sqlite
  sqlite> .import users.csv users2
  users.csv:1: INSERT failed: datatype mismatch
  ```

  

- WHERE문 심화 (users)

  - users에서 age가 30 이상이고, 성이 김인 사람의 이름과 나이만 가져온다면?

    ```sqlite
    SELECT age, first_name FROM users WHERE age >= 30 AND last_name='김';
    ```

- 특정 칼럼에 대한 평균, 최댓값, 최솟값 등을 함수를 이용해서 확인할 수도 있다.

  ```sqlite
  sqlite> SELECT COUNT(*) FROM users;
  1000
  sqlite> SELECT AVG(age) FROM users;
  27.346
  sqlite> SELECT MAX(age) FROM users;
  40
  sqlite> SELECT MIN(age) FROM users;
  15
  sqlite> SELECT AVG(age) FROM users WHERE age >= 30;
  35.1763285024155
  
  ```

- users에서 가장 큰 잔액(balance)을 갖고 있는 사람의 이름은?

- users에서 30살 이상인 사람의 계좌 평균 잔액은?

  ```sqlite
  sqlite> SELECT first_name, MAX(balance) FROM users;
  "선영",990000
  
  sqlite> SELECT AVG(balance) FROM users WHERE age >= 30;
  153541.425120773
  
  ```

## LIKE (wild cards)

- 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환

- 2가지 패턴

  - `_`: 반드시 이 자리에 한 개의 문자가 존재해야 한다.
  - `%`: 이 자리에 문자열이 있을수도, 없을수도 있다.

- |  %   |        2%         |                  2로 시작하는 값                  |
  | :--: | :---------------: | :-----------------------------------------------: |
  |      |        %2         |                   2로 끝나는 값                   |
  |      |        %2%        |                  2가 들어가는 값                  |
  |      |        _2%        | 아무 값이나 들어가고 <br>두번째가 2로 시작하는 값 |
  |      |       1___        |              1로 시작하고 4자리인 값              |
  |      | `2_%_%`, / `2__%` |          2로 시작하고 적어도 3자리인 값           |

- users에서 20대인 사람은?

- users에서 지역번호가 02인 사람들은?

- users에서 이름이 '준'으로 끝나는 사람만?

- users에서 중간 번호가 5114인 사람만?



## ORDER

- users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아보면?

- users에서 나이순, 성 순으로 오름차순 정렬하여 상위 10개만 뽑아보면?

- users에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개만 뽑아보면?

  ```sqlite
  sqlite> SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;
  "선영","김"
  "상현","나"
  "정호","이"
  "상철","이"
  "지아","최"
  "준서","박"
  "미영","문"
  "하윤","고"
  "은정","유"
  "서윤","안"
  ```

- 
  ```sqlite
  sqlite> SELECT * FROM users ORDER BY balance ASC;
  ```



## ALTER

### 테이블명 변경

- 먼저 새로운 테이블 articles를 생성
  title: TEXT NOT NULL
  content: TEXT NOT NULL

  ```sqlite
  sqlite> CREATE TABLE articles (
     ...> title TEXT NOT NULL,
     ...> content TEXT NOT NULL
     ...> );
  ```

- articles 테이블에 값을 넣어보기

  ```sqlite
  
  ```

- 특정 테이블의 이름을 변경하기

- ```sqlite
  sqlite> DROP TABLE users;
  sqlite> .tables
  classmates  tests       users2
  
  ```

- ```sqlite
  sqlite> ALTER TABLE users2 RENAME TO users;
  sqlite> .tables
  articles    classmates  tests       users
  ```
### 새로운 컬럼 추가

```sqlite
sqlite> SELECT * FROM tests;
1|홍길동
3|왕건


sqlite> ALTER TABLE tests ADD COLUMN created_at DATETIME NOT NULL;
Error: Cannot add a NOT NULL column with default value NULL


sqlite> ALTER TABLE tests ADD COLUMN gender TEXT NOT NULL DEFAULT 'female';
sqlite> SELECT * FROM tests;
1|홍길동|female
3|왕건|female

```

- 기존 데이터에 NOT NULL 조건으로 인해 NULL 값으로 새로운 컬럼이 추가될 수 없을 때 발생하는 에러는 NOT NULL 조건을 없애거나, 기본값(DEFAULT)을 지정해야 한다.





---

# 191014 DB 4일차

- CRUD
- 1:N 
- `DRY` 코드의 재사용성을 높이자.
- ------------여기까지 했음, 이제 아래 것들을 할 차례---------------
- Django의 form을 Model Form으로
- Auth + `M:N` 관계 + Validation + Deploy

- admin.py를 다뤄보자
  - 재사용 가능한 코드를 만들어 놓은 것

```python
from django.contrib import admin
from .models import Article

# Register your models here.

# 뭐를 보고 싶은지?
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    list_display_links = ('title',)

admin.site.register(Article, ArticleAdmin)
```

- `Ctrl+Shift+j` 자바스크립트 콘솔창
- 자바스크립트는 브라우저를 조작하는 언어
- django rest framework
- form 모듈화
- forms.py를 만들자

```python
from django import forms

# class Article(models.MOdel)
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()
```

```python
# views.py의 else부분에서 만들어준다.
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        new_article = Article.objects.create(
            title=title,
            content=content,
        )
        print(new_article.pk)
        return redirect(new_article)
    else:
        form = ArticleForm()
        context = {
            'form':form,
        }
        return render(request, 'articles/create.html', context)
```

```html
{% extends 'base.html' %}

{% block body %}
  <h1>새글쓰기(input태그이용)</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    제목: <input type="text" name="title"><br>
    내용: <textarea name="content" id="" cols="30" rows="10"></textarea>
    <input type="submit">
  </form>

  <h2>Form 클래스를 통한 HTML Form 생성</h2>
  <form>
    {{ form.as_p }}
  </form>

{% endblock %}
```

```bash
$ pip install bootstrap4
```

```python
# settings.py의 INSTALLED_APPS에 bootstrap4 추가해주기
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
]
```

- base.html에 아래처럼 만들어줄 수 있다.
- bootstrap에서 Starter Template을 복사붙여넣기 한 것과 같은 과정

```html
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  {% block body %}
  {% endblock %}
</body>
</html>
```

- install한 패키지와 form.py, views.py를 사용해서 create html파일을 아래처럼 바꿔줄 수 있음

```html
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}
<div class="container">
  <h1>새글쓰기(input태그이용)</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit">
  </form>
</div>
```



---

# 191015 5일차

- settings.py에 'django_extentions' 추가

- bash 창에서 `pip install ipython` 설치

- 설치된 패키지 리스트 확인은 bash 창에서 `pip list`로 확인

- ipython은 글로벌로 깔려 있기 때문에 settings에 추가해줄 필요가 없다.

- ```python
  from IPython import embed
  
  ...
  embed()
  ...
  ```

- 장고가 실행되는 data-flow에서 embed 함수를 만나면 실행을 잠시 멈추고 터미널 창에 shell 창을 띄워준다.

- shell은 bash에서 python manage.py shell_plus로 실행하면 보이는 것과 같은 모양

- ```python
  def create(request):
      if request.method == 'POST':
  
          form = ArticleForm(request.POST)
          embed()
  
          # 전송된 데이터가 유효한 값인지 검사
          if form.is_valid():
              title = form.cleaned_data.get('title')
              content = form.cleaned_data.get('content')
              article = Article.objects.create(
                  title=title,
                  content=content,
                  )
              return redirect(article)
          else:
              return redirect('articles:create')
      else:
          form = ArticleForm()
          context = {
              'form':form,
          }
          return render(request, 'articles/create.html', context)
  ```

- create 함수가 불리면 else 부분에서 form 객체 형성.

- ```shell
  In [3]: request.POST
  Out[3]: <QueryDict: {'csrfmiddlewaretoken': ['s5Kd9lTraJ12gQsrg57FgiqJJlOGDgW801lcvMxLwdLJ7uRIxaFLXArFRvjPAAWi'], 'title': ['하하하하하하 Form class 짱이지'], 'content': ['좋아좋아']}>
  
  ```

- ```shell
  In [4]: type(request.POST)
  Out[4]: django.http.request.QueryDict
  ```

- ```shell
  In [5]: request.POST.get('content')
  Out[5]: '좋아좋아'
  ```

- ```shell
  In [6]: request.POST.get('csrfmiddlewaretoken')
  Out[6]: 's5Kd9lTraJ12gQsrg57FgiqJJlOGDgW801lcvMxLwdLJ7uRIxaFLXArFRvjPAAWi'
  
  ```

- ```shell
  In [1]: type(form)
  Out[1]: articles.forms.ArticleForm
  ```

- ```shell
  In [3]: form.is_valid()
  Out[3]: True
  ```

- embed()는 장고 디버깅할 때 유용하게 써먹을 수 있다.

- 사용자는 또라이다

- detail 페이지에 이상한 요청이 들어왔을 경우 처리하는 방법

- ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from .models import Article
  from .forms import ArticleForm
  from django.http import Http404
  
  def detail(request,article_pk):
      # article = get_object_or_404(Article, pk=article_pk), 아래 try~except 4줄 구문으로 바꿔준다.
      
      # 만약에 Article.objects.get(pk=article_pk)가 없으면? try안에 에러가 날 법한 소스를 넣어서 확인
      try:
          article = Article.objects.get(pk=article_pk)
      except Article.DoesNotExist: # 에러가 발생하면 아래를 실행
          raise Http404('해당하는 id의 글이 존재하지 않습니다.')
      
      # 위의 try 구문이 무리 없이 통과되면 아래 코드가 실행될 것
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

- Comment 생성 & 삭제

  - POST /articles/:id/comments
  - POST /articles/:id/comments_delete/:c_id
  - ModelForm 활용