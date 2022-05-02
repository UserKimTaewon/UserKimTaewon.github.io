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
