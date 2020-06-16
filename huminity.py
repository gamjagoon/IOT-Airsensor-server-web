import time, Adafruit_DHT ,socket
DATAPATH = "/home/pi/IOT-Airsensor-server-web/LCD/tmp2.txt"
sensor = Adafruit_DHT.DHT11
pin = 4

def process_data():
    sumh ,sumt = 0.0,0.0
    for i in range(30):
        h,t = Adafruit_DHT.read_retry(sensor, pin)
        sumh += h
        sumt += t
        time.sleep(1)
    sumh = round(sumh/30,2)
    sumt = round(sumt/30,2)
    return sumh,sumt

def data_insert(hum, tem):
    jsonrow = {'hum': hum, 'tem':tem,'time':time.strftime("%Y.%m.%d %H:%M")}
    savedata(jsonrow)


def savedata(values):
    data = str(values['hum'])+" "+str(values['tem'])+" "+time.strftime("%Y.%m.%d %H:%M")
    with open(DATAPATH, "w+") as F:
        F.write(data)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as S:
        S.connect(('algora.iptime.org',30122))
        time.sleep(1)
        S.sendall(data.encode())
        resp = S.recv(64)
        print(resp)

if __name__ == "__main__":
    while True:
        hum,tem = process_data()
        data_insert(hum,tem)
        time.sleep(30)
