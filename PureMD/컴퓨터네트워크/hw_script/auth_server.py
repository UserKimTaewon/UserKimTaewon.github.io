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
User('taewon','1234abc'),
User('kimtaewon','password2'),
User('user','password1234'),
User('dankook','univ42'),
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
                else:
                    break
                inp=conn.recv(4096).decode(encoding=ENCODING)
            adduser(uid,inp)
            send(conn,CLOSE+f'succesfully added user:{uid}')

if __name__=='__main__':
    main()
