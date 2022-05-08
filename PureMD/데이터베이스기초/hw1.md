다른 언어로 짠 쿼리
===
# 실행화면
```idle
>>> Depts.selectnames(('dname','loc')).printline()
{dname=ACCOUNTING,loc=NEW YORK}
{dname=RESEARCH,loc=DALLAS}
{dname=SALES,loc=CHICAGO}
{dname=OPERATIONS,loc=BOSTON}
>>> Emps.selectnames(('ename','job')).printline()
{ename=SMITH,job=CLERK}
{ename=ALLEN,job=SALESMAN}
{ename=WARD,job=SALESMAN}
{ename=JONES,job=MANAGER}
{ename=MARTIN,job=SALESMAN}
{ename=BLAKE,job=MANAGER}
{ename=CLARK,job=MANAGER}
{ename=SCOTT,job=ANALYST}
{ename=KING,job=PRESIDENT}
{ename=TURNER,job=SALESMAN}
{ename=ADAMS,job=CLERK}
{ename=JAMES,job=CLERK}
{ename=FORD,job=ANALYST}
{ename=MILLER,job=CLERK}
>>> Emps.where(lambda x:x.job=='SALESMAN').selectnames(('ename','hiredate')).printline()
{ename=ALLEN,hiredate=1981-02-20}
{ename=WARD,hiredate=1981-02-22}
{ename=MARTIN,hiredate=1981-08-28}
{ename=TURNER,hiredate=1981-08-08}
>>> Emps.where(lambda x:x.hiredate>=date(1982,5,8)).selectnames(('empno','ename','hiredate')).printline()
{empno=7788,ename=SCOTT,hiredate=1982-12-09}
{empno=7876,ename=ADAMS,hiredate=1983-01-12}
>>> Emps.joinfield(Depts,'deptno').selectnames(('ename','dname')).printline()
{ename=SMITH,dname=RESEARCH}
{ename=ALLEN,dname=SALES}
{ename=WARD,dname=SALES}
{ename=JONES,dname=RESEARCH}
{ename=MARTIN,dname=SALES}
{ename=BLAKE,dname=SALES}
{ename=CLARK,dname=ACCOUNTING}
{ename=SCOTT,dname=RESEARCH}
{ename=KING,dname=ACCOUNTING}
{ename=TURNER,dname=SALES}
{ename=ADAMS,dname=RESEARCH}
{ename=JAMES,dname=SALES}
{ename=FORD,dname=RESEARCH}
{ename=MILLER,dname=ACCOUNTING}
>>> Emps.where(lambda x:x.sal>1000).joinfield(Depts,'deptno').selectnames(('ename','sal','dname')).printline()
{ename=ALLEN,sal=1600.00,dname=SALES}
{ename=WARD,sal=1250.00,dname=SALES}
{ename=JONES,sal=2975.00,dname=RESEARCH}
{ename=MARTIN,sal=1250.00,dname=SALES}
{ename=BLAKE,sal=2850.00,dname=SALES}
{ename=CLARK,sal=2450.00,dname=ACCOUNTING}
{ename=SCOTT,sal=3000.00,dname=RESEARCH}
{ename=KING,sal=5000.00,dname=ACCOUNTING}
{ename=TURNER,sal=1500.00,dname=SALES}
{ename=ADAMS,sal=1100.00,dname=RESEARCH}
{ename=FORD,sal=3000.00,dname=RESEARCH}
{ename=MILLER,sal=1300.00,dname=ACCOUNTING}
>>> Emps.where(lambda x:x.hiredate>=date(1982,5,8)).joinfield(Depts,'deptno').selectnames(('empno','ename','dname')).printline()
{empno=7788,ename=SCOTT,dname=RESEARCH}
{empno=7876,ename=ADAMS,dname=RESEARCH}
>>> Depts.where(lambda x:x.loc=='DALLAS').joinfield(Emps,'deptno').selectnames(('ename','sal')).printline()
{ename=SMITH,sal=800.00}
{ename=JONES,sal=2975.00}
{ename=SCOTT,sal=3000.00}
{ename=ADAMS,sal=1100.00}
{ename=FORD,sal=3000.00}
>>> Emps.where(lambda x:x.sal<1000 and x.hiredate<date(1982,5,8)).joinfield(Depts,'deptno').selectnames(('empno','ename','dname')).printline()
{empno=7369,ename=SMITH,dname=RESEARCH}
{empno=7900,ename=JAMES,dname=SALES}
>>> 
```
# 소스코드
## pyQuarry.py
```python
from itertools import starmap

__all__='samefield','Nothing','Table'


def samefield(name1,name2):
    return lambda x,y:getattr(x,name1)==getattr(y,name2)

class Table(list):
    @classmethod
    def from_constructor(cls,constructor,args):
        return cls(starmap(constructor,args))
    def join(x,y,f):
        return type(x)(((i,j) for i in x for j in y if f(i,j)))
    
    def joinfield(x,y,fname):
        same=samefield(fname,fname)
        return type(x)((ChainAttr(i,j) for i in x for j in y if same(i,j)))

    def select(x,f):
        return type(x)(map(f,x))
    
    def selectnames(x,names):
        names=tuple(names)
        return type(x)((LimitAttr(i,names) for i in x))
    
    def where(x,f):
        return type(x)(filter(f,x))
    def printline(x):
        for i in x:
            print(i)

class Nothing:
    nofn=lambda *args:Nothing
    __radd__=__rmul__=__rsub__=__lt__=nofn

Nothing=Nothing()

class LimitAttr:
    __slots__='__origin','__acceptable'
    def __init__(self,origin,acceptable):
        self.__origin=origin
        self.__acceptable=acceptable
    def __getattr__(self,field):
        if field in self.__acceptable:
            return getattr(origin,field)
    def __repr__(self):
        return '{'+','.join((f+'='+str(getattr(self.__origin,f)) for f in self.__acceptable))+'}'

class ChainAttr:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def __getattr__(self,field):
        res=getattr(self.__x,field,Nothing)
        if res is not Nothing:
            return res
        res=getattr(self.__y,field,Nothing)
        if res is not Nothing:
            return res
```
## pyQuarryTest.py
```python
from dataclasses import dataclass,fields
from datetime import date
from decimal import Decimal
from typing import Optional
import itertools

from pyQuarry import Table

#def print_dataclass(x,knownfields=None):
#    knownfields=knownfields or fields(x)
#    for f in knownfields:
#        strs
def print_list(x):
    for i in x:
        print(i)


@dataclass
class Dept:
    deptno:int
    dname:str
    loc:str
    def __post_init__(self):
        self.deptno=int(self.deptno)

@dataclass
class Emp:
    empno:int
    ename:str
    job:str
    mgr:Optional[int]
    hiredate:date
    sal:Decimal
    comm:Optional[Decimal]
    deptno:int
    def __post_init__(self):
        self.empno=int(self.empno)
        if isinstance(self.mgr,str):
            self.mgr=int(self.mgr)
        if isinstance(self.hiredate,str):
            self.hiredate=date.fromisoformat(self.hiredate)
        if isinstance(self.sal,str):
            self.sal=Decimal(self.sal)
        if isinstance(self.comm,str):
            self.comm=Decimal(self.comm)
        self.deptno=int(self.deptno)

Depts=Table.from_constructor(Dept,[
(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH', 'DALLAS'),
(30, 'SALES', 'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON')
])
Emps=Table.from_constructor(Emp,[
(7369 ,'SMITH', 'CLERK', '7902', '1980-12-17', '800.00', None, '20'),
(7499, 'ALLEN', 'SALESMAN', '7698', '1981-02-20', '1600.00', '300.00', '30'),
(7521, 'WARD', 'SALESMAN', '7698', '1981-02-22', '1250.00', '500.00', '30'),
(7566, 'JONES', 'MANAGER', '7839', '1981-04-02', '2975.00', None, '20'),
(7654, 'MARTIN', 'SALESMAN', '7698', '1981-08-28', '1250.00', '1400.00', '30'),
(7698, 'BLAKE', 'MANAGER', '7839', '1981-05-01', '2850.00', None, '30'),
(7782, 'CLARK', 'MANAGER', '7839', '1981-06-09', '2450.00', None, '10'),
(7788, 'SCOTT', 'ANALYST', '7566', '1982-12-09', '3000.00', None, '20'),
(7839, 'KING', 'PRESIDENT', None, '1981-11-17', '5000.00', None, '10'),
(7844, 'TURNER', 'SALESMAN', '7698', '1981-08-08', '1500.00', '0.00', '30'),
(7876, 'ADAMS', 'CLERK', '7788', '1983-01-12', '1100.00', None, '20'),
(7900, 'JAMES', 'CLERK', '7698', '1981-12-03', '950.00', None, '30'),
(7902, 'FORD', 'ANALYST', '7566', '1981-12-03', '3000.00', None, '20'),
(7934, 'MILLER', 'CLERK', '7782', '1982-01-23', '1300.00', None, '10')
])
```
