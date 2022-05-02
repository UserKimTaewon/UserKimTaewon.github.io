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
