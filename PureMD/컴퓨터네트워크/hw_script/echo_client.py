import socket
ENCODING='utf8'
PORT=4224

def main(port=PORT,host='localhost'):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        print(f'connecting to {host}:{port}')
        while True:
            inp=input('[Client]>')
            try:
                res=sock.sendall(inp.encode(encoding=ENCODING))
                data=sock.recv(4096).decode(encoding=ENCODING)
                print(f'[Server]>{data}')
            except socket.error:
                print('an error occured during connection')
                return

if __name__=='__main__':
    main()
