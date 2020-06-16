import socket,sys,time

def run():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as S:
        S.connect(('algora.iptime.org',30122))
        data = "1.22 1.23 52.6 29.87 2020.06.16 23:44"
        time.sleep(1)
        S.sendall(data.encode())
        resp = S.recv(64)
        print(resp)

if __name__ == "__main__":
    run()