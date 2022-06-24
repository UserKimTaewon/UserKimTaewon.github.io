sqlite3의 주의 사항
===

# 서론
python에 기본 라이브러리에 sqlite3이 있어 sql관련 과제를 따로 DBMS를 설치하지 않고 sqlite3으로 해보려고 했다.

하지만 sqlite3에 대해 찾아볼수록 SQL을 사용 가능한 무언가는 맞지만 다른 DBMS와는 너무 다른 점이 눈에 보였다.

# sqlite3에 대한 간략한 설명
SQL로 질의가 가능한 
파일 기반 DBMS?이다.
## 주의사항
[홈페이지](https://sqlite.org/whentouse.html)와 다른 곳에서도 경고하지만

> sqlite는 다른 DBMS와 경쟁하는 것이 아니라 오히려 fopen과 경쟁한다.

즉, sqlite는 다른 DBMS의 대체로 사용하면 안되고,

오히려 파일에 정보를 저장하려고 하는데 거기에 무결성 제약조건을 넣거나, table을 만들거나, SQL로 쿼리를 하는 등의 고급 기능이 필요하면 선택하는 것이다.

sqlite 대신 사용 가능한 건 다른 DBMS가 아니라 xml,json, 파이썬의 pickle 등의 객체 직렬화 프로토콜들 이다.

## 장점
가볍고 작다.
- DBMS 프로세스가 따로 생성되는 게 아니라 바로 파일에 읽고 쓴다.

## 단점
단 한명의 유저만 사용 가능하다.
즉, 다른 DBMS와는 다르게 동시성 제어,접근 제어 등이 없이 파일을 연 프로세스만 DB에 접속 가능하다.

# 이상해 보였던 점들.
## 1.날짜 자료형
sqlite에는 날짜 자료형이 없다.
문자열 TEXT
바이트열 BLOB
정수 INTEGER
실수 FLOAT
가 사용 가능한 모든 데이터형이다.
하지만 날짜 관련 함수는 존재한다.

이 날짜 함수들은 
`YYYY-MM-DD`
형식으로 포맷된 문자열등 날짜처럼 사용한다.
예를 들어 2022년 6월 2일의 3일 전 날짜를 구하고 싶다면

```SQL
SELECT date('2022-06-02','-3 day');
```

|date('2022-06-02','-3 day')|
|---------------------------|
|                 2022-05-30|

처럼 하면 된다.

정확하게 말하자면 [홈페이지](https://www.sqlite.org/lang_datefunc.html)에 따르면
> text in a subset of the ISO-8601 format,
> numbers representing the Julian day, or
> numbers representing the number of seconds since (or before) 1970-01-01 00:00:00 UTC (the unix timestamp). 

를 날짜/시간 함수가 받아들이는 것 같다.

## 2.동적 타이핑
말 그대로 sqlite는 동적 타이핑을 지원한다.
```SQL
CREATE TABLE DEPT(DEPTNO INTEGER, DNAME TEXT, LOC TEXT);
```
처럼 TABLE을 만들 수도 있지만, 여기서 타입 정보는 완전히 무시되는 것 같다.
```SQL
CREATE TABLE DEPT(DEPTNO, DNAME, LOC);
```
처럼 타입을 명시 안해도 아무런 문제도,차이도 없는 것이다.
그래서 
```SQL
INSERT INTO DEPT VALUES (42,77,3.14);
```
같은 걸 해도 아무런 문제 없이 잘 실행이 된다...
