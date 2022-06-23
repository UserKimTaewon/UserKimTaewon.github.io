SQL 과제
===

# db 초기화
단, 매 실행은 `python shell.py shelltest.db`으로 db에 접속하였다.
sqlite3으로 하려다 보니 world database는 기본 제공이 아니고, 용량도 너무 커 손으로 직접 입력이 불가능해
관련 문제는 제외하였다.
```idle
Enter your SQL commands to execute in sqlite3.
Enter 'QUIT' or 'quit' or 'EXIT' or 'exit' to exit.
>>>CREATE TABLE DEPT(
...DEPTNO INTEGER PRIMARY KEY,
...DNAME TEXT NOT NULL,
...LOC TEXT NOT NULL
...);
>>>INSERT INTO DEPT VALUES (10,'ACCOUNTING','NEW YORK'),(20,'RESEARCH','DALLAS'),(30,'SALES','CHICAGO'),(40,'OPERATIONS','BOSTON');
>>>SELECT * FROM DEPT;
+------+----------+--------+
|DEPTNO|     DNAME|     LOC|
+------+----------+--------+
|    10|ACCOUNTING|NEW YORK|
|    20|  RESEARCH|  DALLAS|
|    30|     SALES| CHICAGO|
|    40|OPERATIONS|  BOSTON|
+------+----------+--------+
>>>CREATE TABLE EMP(
...EMPNO INTEGER PRIMARY KEY AUTOINCREMENT,
...ENAME TEXT NOT NULL,
...JOB TEXT NOT NULL,
...MGR INTEGER,
...HIREDATE DATE NOT NULL,
...SAL REAL NOT NULL,
...COMM REAL,
...DEPTNO INTEGER NOT NULL,
...FOREIGN KEY(MGR) REFERENCES EMP(EMPNO),
...FOREIGN KEY(DEPTNO) REFERENCES DEPT(DEPTNO)
...);
>>>INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,'1980-12-17',800.0,NULL,20),
...(7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600.0,300.0,30),
...(7521,'WARD','SALESMAN',7698,'1981-02-22',1250.0,500.0,30),
...(7566,'JONES','MANAGER',7839,'1981-04-02',2975.0,NULL,20),
...(7654,'MARTIN','SALESMAN',7698,'1981-08-28',1250.0,1400.0,30),
...(7698,'BLAKE','MANAGER',7839,'1981-05-01',2850.0,NULL,30),
...(7782,'CLARK','MANAGER',7839,'1981-06-09',2450.0,NULL,10),
...(7788,'SCOTT','ANALYST',7566,'1982-12-09',3000.0,NULL,20),
...(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000.0,NULL,10),
...(7844,'TURNER','SALESMAN',7698,'1981-08-08',1500.0,0.0,30),
...(7876,'ADAMS','CLERK',7788,'1983-01-12',1100.0,NULL,20),
...(7900,'JAMES','CLERK',7698,'1981-12-03',950.0,NULL,30),
...(7902,'FORD','ANALYST',7566,'1981-12-03',3000.0,NULL,20),
...(7934,'MILLER','CLERK',7782,'1982-01-23',1300.0,NULL,10);
>>>SELECT * FROM EMP;
+-----+------+---------+----+----------+------+------+------+
|EMPNO| ENAME|      JOB| MGR|  HIREDATE|   SAL|  COMM|DEPTNO|
+-----+------+---------+----+----------+------+------+------+
| 7369| SMITH|    CLERK|7902|1980-12-17| 800.0|  NULL|    20|
| 7499| ALLEN| SALESMAN|7698|1981-02-20|1600.0| 300.0|    30|
| 7521|  WARD| SALESMAN|7698|1981-02-22|1250.0| 500.0|    30|
| 7566| JONES|  MANAGER|7839|1981-04-02|2975.0|  NULL|    20|
| 7654|MARTIN| SALESMAN|7698|1981-08-28|1250.0|1400.0|    30|
| 7698| BLAKE|  MANAGER|7839|1981-05-01|2850.0|  NULL|    30|
| 7782| CLARK|  MANAGER|7839|1981-06-09|2450.0|  NULL|    10|
| 7788| SCOTT|  ANALYST|7566|1982-12-09|3000.0|  NULL|    20|
| 7839|  KING|PRESIDENT|NULL|1981-11-17|5000.0|  NULL|    10|
| 7844|TURNER| SALESMAN|7698|1981-08-08|1500.0|   0.0|    30|
| 7876| ADAMS|    CLERK|7788|1983-01-12|1100.0|  NULL|    20|
| 7900| JAMES|    CLERK|7698|1981-12-03| 950.0|  NULL|    30|
| 7902|  FORD|  ANALYST|7566|1981-12-03|3000.0|  NULL|    20|
| 7934|MILLER|    CLERK|7782|1982-01-23|1300.0|  NULL|    10|
+-----+------+---------+----+----------+------+------+------+
>>>quit
```
# 실습과제 1
## 2. DALLAS 에서 근무하는 사원중 연봉이 4000 이하인 사람은 몇 명인가

```SQL
SELECT COUNT(*) FROM EMP WHERE SAL<4000;
```

|COUNT(*)|
|--------|
|      13|

## 5. 모든 매니저의 이름과 부하직원의 숫자를 보이시오
```sql
SELECT M.ENAME,COUNT(E.EMPNO)
FROM EMP AS M,EMP AS E
WHERE M.EMPNO=E.MGR
GROUP BY M.EMPNO;
```

|ENAME|COUNT(E.EMPNO)|
|-----|--------------|
|JONES|             2|
|BLAKE|             5|
|CLARK|             1|
|SCOTT|             1|
| KING|             3|
| FORD|             1|

## 6. 각 지역별로 근무하는 사원들의 연봉 합계를 보이시오 (지역명, 연봉합계)
```sql
SELECT D.LOC,SUM(E.SAL)
FROM EMP AS E,DEPT AS D
WHERE E.DEPTNO=D.DEPTNO
GROUP BY D.LOC;
```

|     LOC|SUM(E.SAL)|
|--------|----------|
| CHICAGO|    9400.0|
|  DALLAS|   10875.0|
|NEW YORK|    8750.0|

## 7. 매니저가 아닌 (부하직원이 없는) 사원들은 몇 명인가?
```sql
SELECT COUNT(*)
FROM EMP AS M
WHERE NOT EXISTS(
SELECT *FROM EMP AS E
WHERE E.MGR=M.EMPNO
);
```

|COUNT(*)|
|--------|
|       8|

## 8. 매니저가 아닌 (부하직원이 없는) 사원들의 연봉합계는 얼마인가
```sql
SELECT SUM(M.SAL)
FROM EMP AS M
WHERE NOT EXISTS(
SELECT *FROM EMP AS E
WHERE E.MGR=M.EMPNO
);
```

|SUM(M.SAL)|
|----------|
|    9750.0|

## 9. 매니저이름, 부하직원이름, 부서명 을 보이시오 (매니저이름으로 정렬)
```sql
SELECT M.ENAME,E.ENAME,D.DNAME
FROM EMP AS M,EMP AS E,DEPT AS D
WHERE M.EMPNO=E.MGR AND M.DEPTNO=D.DEPTNO
ORDER BY M.ENAME;
```

|ENAME| ENAME|     DNAME|
|-----|------|----------|
|BLAKE| ALLEN|     SALES|
|BLAKE|  WARD|     SALES|
|BLAKE|MARTIN|     SALES|
|BLAKE|TURNER|     SALES|
|BLAKE| JAMES|     SALES|
|CLARK|MILLER|ACCOUNTING|
| FORD| SMITH|  RESEARCH|
|JONES| SCOTT|  RESEARCH|
|JONES|  FORD|  RESEARCH|
| KING| JONES|ACCOUNTING|
| KING| BLAKE|ACCOUNTING|
| KING| CLARK|ACCOUNTING|
|SCOTT| ADAMS|  RESEARCH|

# 실습과제 2
## 2. 연봉을 평균 이상 받는 사원들의 이름, 연봉, 근무지를 보이시오
```sql
SELECT ENAME,SAL,LOC
FROM EMP,DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
	AND EMP.SAL>=(SELECT AVG(SAL) FROM EMP);
```

|ENAME|   SAL|     LOC|
|-----|------|--------|
|JONES|2975.0|  DALLAS|
|BLAKE|2850.0| CHICAGO|
|CLARK|2450.0|NEW YORK|
|SCOTT|3000.0|  DALLAS|
| KING|5000.0|NEW YORK|
| FORD|3000.0|  DALLAS|

## 3. 연봉을 가장 적게 받는 사원의 매니저는 누구인가? 
```sql
SELECT M.ENAME
FROM EMP AS E,EMP AS M
WHERE E.MGR=M.EMPNO AND E.SAL=(SELECT MIN(SAL) FROM EMP);
```

|ENAME|
|-----|
| FORD|

## 4. 연봉을 가장 많이 받는 사원과 적게 받는 사원의 이름, 연봉을 보이시오
```sql
SELECT ENAME,SAL
FROM EMP
WHERE SAL IN ((SELECT MAX(SAL) FROM EMP),(SELECT MIN(SAL) FROM EMP));
```

|ENAME|   SAL|
|-----|------|
|SMITH| 800.0|
| KING|5000.0|

## 5. 연봉을 가장 많이 받는 사원과 적게 받는 사원을 제외한 나머지 사원들의 총 연봉 합계를 보이시오
```sql
SELECT AVG(SAL)
FROM EMP
WHERE SAL NOT IN ((SELECT MAX(SAL) FROM EMP),(SELECT MIN(SAL) FROM EMP));
```

|          AVG(SAL)|
|------------------|
|1935.4166666666667|

## 6. SALES 부서에 속한 사원들과 동일한 담당업무를 갖는 사원들의 이름, 담당업무를 보이시오 (단 SALES 부서에 속한 사원은 제외)
```sql
SELECT E.ENAME,E.JOB
FROM EMP AS E
WHERE E.JOB IN (
	SELECT DISTINCT SALES.JOB
	FROM EMP AS SALES
	WHERE SALES.DEPTNO IN(
  SELECT DEPTNO FROM DEPT WHERE DNAME='SALES'
	)
) AND E.DEPTNO NOT IN (
	SELECT DEPTNO FROM DEPT WHERE DNAME='SALES'
);
```

| ENAME|    JOB|
|------|-------|
| SMITH|  CLERK|
| JONES|MANAGER|
| CLARK|MANAGER|
| ADAMS|  CLERK|
|MILLER|  CLERK|

## 7. 연봉을 평균보다 500 이상 적게 받는 사원들의 이름, 부서명, 연봉을 보이시오
```sql
SELECT ENAME,DNAME,SAL
FROM EMP,DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
	AND SAL<=(SELECT AVG(SAL) FROM EMP)-500;
```

| ENAME|     DNAME|   SAL|
|------|----------|------|
| SMITH|  RESEARCH| 800.0|
|  WARD|     SALES|1250.0|
|MARTIN|     SALES|1250.0|
|TURNER|     SALES|1500.0|
| ADAMS|  RESEARCH|1100.0|
| JAMES|     SALES| 950.0|
|MILLER|ACCOUNTING|1300.0|

## 8. JAMES 보다 입사일이 빠른 사원들의 이름, 담당업무, 입사일을 보이시오
```sql
SELECT ENAME,JOB,HIREDATE
FROM EMP
WHERE HIREDATE<(
	SELECT HIREDATE
	FROM EMP
	WHERE ENAME='JAMES'
);
```

| ENAME|      JOB|  HIREDATE|
|------|---------|----------|
| SMITH|    CLERK|1980-12-17|
| ALLEN| SALESMAN|1981-02-20|
|  WARD| SALESMAN|1981-02-22|
| JONES|  MANAGER|1981-04-02|
|MARTIN| SALESMAN|1981-08-28|
| BLAKE|  MANAGER|1981-05-01|
| CLARK|  MANAGER|1981-06-09|
|  KING|PRESIDENT|1981-11-17|
|TURNER| SALESMAN|1981-08-08|

## 9. ADAMS 보다 연봉을 많이 받는 사람은 모두 몇명인가
```sql
SELECT COUNT(E.EMPNO)
FROM EMP AS ADAMS,EMP AS E
WHERE ADAMS.ENAME='ADAMS' AND E.SAL>ADAMS.SAL
GROUP BY ADAMS.EMPNO;
```

|COUNT(E.EMPNO)|
|--------------|
|            11|
# 실습과제 3
## 3. SCOTT 보다 연봉을 많이 받는 사람들 중에서 SCOTT 와 연봉이 비슷한 사람 3명의 이름, 부서명, 연봉을 보이시오
```sql
SELECT ENAME,DNAME,SAL
FROM EMP,DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
	AND SAL>(SELECT SAL FROM EMP WHERE ENAME='SCOTT')
ORDER BY SAL
LIMIT 3;
```

|ENAME|     DNAME|   SAL|
|-----|----------|------|
| KING|ACCOUNTING|5000.0|

SCOTT 보다 연봉을 많이 받는 사람이 단 1명 뿐이었다.

## 4.BLAKE 보다 입사일이 늦은 사람들 중에서 상위 2명을 제외하고 3명의 이름, 부서명, 입사일자를 보이시오 (입사일자가 빠른순으로)
```sql
SELECT ENAME,DNAME,HIREDATE
FROM EMP,DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
	AND HIREDATE>(SELECT HIREDATE FROM EMP WHERE ENAME='BLAKE')
ORDER BY HIREDATE
LIMIT 2,3;
```

| ENAME|     DNAME|  HIREDATE|
|------|----------|----------|
|MARTIN|     SALES|1981-08-28|
|  KING|ACCOUNTING|1981-11-17|
| JAMES|     SALES|1981-12-03|

## 5.연봉금액이 SMITH 와 FORD 사이인 사원의 이름, 연봉을 보이시오. (단 SMITH 와 FORD 는 누가 더연봉을 많이 받는지 알 수 없다) 
```sql
SELECT E.ENAME,E.SAL
FROM EMP AS E
WHERE E.SAL BETWEEN (SELECT MIN(SAL) FROM EMP
	WHERE ENAME IN ('FORD','SMITH')
) AND (SELECT MAX(SAL) FROM EMP
	WHERE ENAME IN ('FORD','SMITH')
);
```

| ENAME|   SAL|
|------|------|
| SMITH| 800.0|
| ALLEN|1600.0|
|  WARD|1250.0|
| JONES|2975.0|
|MARTIN|1250.0|
| BLAKE|2850.0|
| CLARK|2450.0|
| SCOTT|3000.0|
|TURNER|1500.0|
| ADAMS|1100.0|
| JAMES| 950.0|
|  FORD|3000.0|
|MILLER|1300.0|

## 6.소속된 사원의 연봉 총액이 많은 상위 2개의 부서의 이름과, 연봉 총액을 보이시오
```sql
SELECT DNAME,SUM(SAL)
FROM DEPT,EMP
WHERE EMP.DEPTNO=DEPT.DEPTNO
GROUP BY DEPT.DEPTNO
ORDER BY SUM(SAL) DESC
LIMIT 2;
```

|   DNAME|SUM(SAL)|
|--------|--------|
|RESEARCH| 10875.0|
|   SALES|  9400.0|

# 소스코드
## shell.py
```python
import sqlite3

def max_col(x,leng):
    tmp=[0]*leng
    for items in x:
        for i,item in enumerate(items):
            tmp[i]=max(tmp[i],len(str(item)))
    return tmp

def pprint(keys:list[str],items:list[sqlite3.Row],justfn:'Callable[[str,int],str]'=str.rjust):
    from itertools import chain
    maxl=max_col(chain((keys,),items),len(keys))
    linesep='+'+'+'.join(('-'*l for l in maxl))+'+'
    
    print(linesep)
    print('',*map(justfn,keys,maxl),'',sep='|')
    print(linesep)
    for i in items:
        print('',*(justfn(str(k)if k is not None else 'NULL',l) for k,l in zip(i,maxl)),'',sep='|')
    print(linesep)

def shell(cur:sqlite3.Cursor,quitword=('QUIT','quit','EXIT','exit')):
    print("Enter your SQL commands to execute in sqlite3.")
    print(f"Enter {' or '.join(map(repr,quitword))} to exit.")

    while True:
        buffer = input('>>>')
        if buffer in quitword:
                return
        while not sqlite3.complete_statement(buffer):
            buffer+='\n'+input('...')
            #buffer = buffer.strip()
        try:
            cur.execute(buffer)
            #if buffer.lstrip().upper().startswith("SELECT"):
            #    print(cur.fetchall())
            res=cur.fetchall()
            if res:
                pprint(res[0].keys(),res)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""
def connect(db=':memory:'):
    con = sqlite3.connect(db)
    con.isolation_level = None
    con.execute('PRAGMA foreign_keys = ON;')
    con.row_factory=sqlite3.Row
    return con
def integrity_check(cur):
    res=con.execute('PRAGMA INTEGRITY_CHECK;').fetchone()
    assert tuple(res)==('ok',),f'integrity check failed'

if __name__=='__main__':
    import sys
    db=':memory:' if len(sys.argv)==1 else sys.argv[2]
    con = connect(db)
    integrity_check(con)
    shell(con.cursor())
    con.commit()
    con.close()
```
