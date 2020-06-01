import time
import Adafruit_DHT
import dbconfig as db

sensor = Adafruit_DHT.DHT11
pin = 4

def process_data():
    sumh ,sumt = 0.0,0.0
    for i in range(25):
        h,t = Adafruit_DHT.read_retry(sensor, pin)
        print 'huminity : {0} temperature : {1}'.format(h,t)
        sumh += h
        sumt += t
        time.sleep(2)
    sumh = round(sumh/25,2)
    sumt = round(sumt/25,2)
    return sumh,sumt

def db_insert(hum, tem):
    # conn = db.conn_db('hum.db')
    # jsonrow = {'hum': hum, 'temper':tem,'time':time.strftime("%Y.%m.%d %H:%M")}
    # db.insert_hum_db(conn, **jsonrow)
    # conn.close()
    print("db insert",hum,tem)

if __name__ == "__main__":
    while True:
        hum,tem = process_data()
        db_insert(hum,tem)
        time.sleep(9.5)