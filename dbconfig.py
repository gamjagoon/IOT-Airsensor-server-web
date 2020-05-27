import sqlite3

def conn_db(name):
    return sqlite3.connect(name)

def create_db(conn):
    c = conn.cursor()
    c.execute("""CREATE TABLE data
             (hum real, tem real, time text)""")

def insert_db(conn,pm10,pm25,time):
    c = conn.cursor()
    c.execute('INSERT INTO data VALUES (?,?,?)',(pm10,pm25,time))
    conn.commit()

def insert_hum_db(conn,hum,tem,time):
    c = conn.cursor()
    c.execute('INSERT INTO data VALUES (?,?,?)',(hum,tem,time))
    conn.commit()

def close_db(conn):
    conn.close()
