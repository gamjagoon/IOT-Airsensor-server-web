import sqlite3

def conn_db(name):
    return sqlite3.connect(name)

def create_table(conn):
    c = conn.cursor()
    c.execute("""CREATE TABLE humdata
             (hum real, tem real, time text);""")

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def insert_db(conn,pm10,pm25,time):
    c = conn.cursor()
    c.execute('INSERT INTO data VALUES (?,?,?)',(pm10,pm25,time))
    conn.commit()

def insert_hum_db(conn,hum,tem,time):
    c = conn.cursor()
    c.execute('INSERT INTO hum VALUES (?,?,?)',(hum,tem,time))
    conn.commit()

def close_db(conn):
    conn.close()
