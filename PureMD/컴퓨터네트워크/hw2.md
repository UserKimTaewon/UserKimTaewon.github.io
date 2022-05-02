로그인 서버
===
# 실행시
## auth_client.py
```
connecting to localhost:4224
[Server]>enter your id
[Client]>dankook0
[Server]>existing user. enter your password
[Client]>univ32
[Server]>worng password, try again
[Client]>univ42
[Server]>Succesfully logged in
Server is closing connection
```
```
connecting to localhost:4224
[Server]>enter your id
[Client]>unnamed
[Server]>not existing user. enter your password to add new user
[Client]>unnamed
[Server]>password must contain more than 1 numlic charactor
[Client]>1234
[Server]>password must contain more than 1 alphabet charactor
[Client]>un named 1234
[Server]>password must not contain blank charactor
[Client]>unnamed1234
[Server]>succesfully added user:unnamed
Server is closing connection
```
```
connecting to localhost:4224
[Server]>enter your id
[Client]>unnamed
[Server]>existing user. enter your password
[Client]>really
[Server]>worng password, try again
[Client]>1234
[Server]>worng password, try again
[Client]>unnamed1234
[Server]>Succesfully logged in
Server is closing connection
```
## auth_server.py
```
connection from ('127.0.0.1', 64452)
connection from ('127.0.0.1', 64453)
connection from ('127.0.0.1', 64461)
```
# 소스
## auth_client.py
```python
import socket
ENCODING='utf8'
PORT=4224

CLOSE='<<close>>'

def main(port=PORT,host='localhost'):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        print(f'connecting to {host}:{port}')
        while True:
            try:
                data=sock.recv(4096).decode(encoding=ENCODING)
                if data.startswith(CLOSE):
                    print(f"[Server]>{data.replace(CLOSE,'')}")
                    print('Server is closing connection')
                    return
                print(f'[Server]>{data}')
                inp=input('[Client]>')
                res=sock.sendall(inp.encode(encoding=ENCODING))
            except socket.error:
                print('an error occured during connection')
                return

if __name__=='__main__':
    main()
```
## auth_server.py
```python
import socket
import threading
from dataclasses import dataclass

ENCODING='utf8'
PORT=4224
CLOSE='<<close>>'

@dataclass
class User:
    id:str
    pwd:str

users=[
User('taewon2','1234abc'),
User('kimtaewon1','password2'),
User('user32','password1234'),
User('dankook0','univ42'),
]
def get_user(id):
    for u in users:
        if u.id==id:
            return u
    return None

def adduser(id,pwd):
    users.append(User(id,pwd))

def main(port=PORT,host='localhost',listen=5):
    host=host or socket.gethostname()
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.bind((host,port))
        sock.listen(listen)
        while True:
            conn,addr=sock.accept()
            threading.Thread(target=handle,args=(conn,)).run()
            print('connection from',addr)
def send(conn,inp):
    return conn.sendall(inp.encode(encoding=ENCODING))
def handle(conn):
    with conn:
        send(conn,'enter your id')
        uid=conn.recv(4096).decode(encoding=ENCODING)
        user=get_user(uid)
        if user is not None:
            send(conn,'existing user. enter your password')
            inp=conn.recv(4096).decode(encoding=ENCODING)
            while inp!=user.pwd:
                send(conn,'worng password, try again')
                inp=conn.recv(4096).decode(encoding=ENCODING)
            send(conn,CLOSE+'Succesfully logged in')
        else:
            send(conn,'not existing user. enter your password to add new user')
            inp=conn.recv(4096).decode(encoding=ENCODING)
            while True:
                if any(map(str.isspace,inp)):
                    send(conn,'password must not contain blank charactor')
                elif not any(map(str.isnumeric,inp)):
                    send(conn,'password must contain more than 1 numlic charactor')
                elif not any(map(str.isalpha,inp)):
                    send(conn,'password must contain more than 1 alphabet charactor')
                elif len(inp)<=4:
                    send(conn,'password must be longer than 4 charactor')
                else:
                    break
                inp=conn.recv(4096).decode(encoding=ENCODING)
            adduser(uid,inp)
            send(conn,CLOSE+f'succesfully added user:{uid}')

if __name__=='__main__':
    main()

```
