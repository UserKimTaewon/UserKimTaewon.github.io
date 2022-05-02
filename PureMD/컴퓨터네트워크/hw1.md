에코-대문자-서버
===
# 실행시
## echo_client.py
```
connecting to localhost:4224
[Client]>UPPER to LOWER, Converting...
[Server]>upper TO lower, cONVERTING...
```
## echo_upper_server.py
```
recived:UPPER to LOWER, Converting...
connection from ('127.0.0.1', 64419)
```
# 소스
## echo_client.py
```python
import socket
ENCODING='utf8'
PORT=4224

def main(port=PORT,host='localhost'):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        print(f'connecting to {host}:{port}')
        inp=input('[Client]>')
        try:
            res=sock.sendall(inp.encode(encoding=ENCODING))
            data=sock.recv(4096).decode(encoding=ENCODING)
            print(f'[Server]>{data}')
        except socket.error:
            print('an error occured during connection')

if __name__=='__main__':
    main()
```
## echo_upper_server.py
```python
import socket
import threading

ENCODING='utf8'
PORT=4224

def main(port=PORT,host='localhost',listen=5):
    host=host or socket.gethostname()
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.bind((host,port))
        sock.listen(listen)
        while True:
            conn,addr=sock.accept()
            threading.Thread(target=handle,args=(conn,)).run()
            print('connection from',addr)
def handle_one_str(s):
    if s.isupper():
        return s.lower()
    elif s.islower():
        return s.upper()
    else:
        return s
def handle(conn):
    with conn:
        inp=conn.recv(4096).decode(encoding=ENCODING)
        print(f'recived:{inp}')
        inp=''.join(map(handle_one_str,inp))
        conn.sendall(inp.encode(encoding=ENCODING))

if __name__=='__main__':
    main()

```
