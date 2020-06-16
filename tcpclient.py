import socket,sys,time

def run(data):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as S:
        S.connect(('algora.iptime.org',30122))
        time.sleep(1)
        S.sendall(data.encode())
        resp = S.recv(64)
        print(resp)

if __name__ == "__main__":
    while True :
        try:
            run()
        finally:
            pass
