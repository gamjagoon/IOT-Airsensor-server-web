import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()

Datatype = ["pm10 ","pm25 ","hum ","tem "]
PrefixList = ["ug/m3","ug/m3","%","C"]
while 1 :
    f = open('./tmp.txt',mode='r')
    values = list(f.readline().split())
    values = values[0:4]
    f.close()
    strs = []
    for i in range(4) :
        strs.append(Datatype[i] + values[i] + PrefixList[i])
    for i in range(15):
        mylcd.lcd_display_string(strs[0],1)
        mylcd.lcd_display_string(strs[1],2)
        sleep(2)
        mylcd.lcd_clear()
        mylcd.lcd_display_string(strs[2],1)
        mylcd.lcd_display_string(strs[3],2)
        sleep(2)
        mylcd.lcd_clear()


