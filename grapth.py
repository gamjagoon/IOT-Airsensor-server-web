import sqlite3
from time import strftime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib as mpl

DBPATH = "/home/pi/IOT-Airsenser-server-web/pmdata.db"
fname = "/home/pi/IOT-Airsenser-server-web/src/contents/pm_data/logo.png"

if __name__ == "__main__":
    plt.rc('font', family='DejaVu Sans Mono')
    conn = sqlite3.connect(DBPATH)
    c = conn.cursor()
    symbol = strftime("%Y.%m.%d")
    symbol =symbol + " __:00"
    row = c.execute("SELECT * FROM data WHERE time LIKE (:path)",{"path":symbol} ).fetchmany(24)
    row = np.array(row)
    # for val in row:
    #     val[0] = float(val[0])
    #     val[1] = float(val[1])
    t = len(row)
    x = np.arange(0,t)
    pm10 = np.empty([t,])
    pm25 = np.empty([t,])
    for i in range(t):
        pm10[i] = row[i][0]
        pm25[i] = row[i][1]
    fig, ax = plt.subplots()

    line1, = ax.plot(x, pm10, label='pm10 ')
    line1.set_dashes([2, 2, 10, 2])
    line2, = ax.plot(x, pm25, dashes=[6, 2], label='pm2.5 ')
    ax.legend()
    fig.savefig('/home/pi/IOT-Airsenser-server-web/src/contents/pm_data/logo.png')
    conn.close()
