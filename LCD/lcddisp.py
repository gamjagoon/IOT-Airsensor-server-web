import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()
pm10 = "pm10 "
pm25 = "pm25 "
hum = "hum "
tem = "tem "
prefix2 = "'C"
prefix = "ug/m3"
while 1 :
    f1 = open('./tmp.txt',mode='r')
    value_pm = f1.readline().split()
    f1.close()
    f2 = open('./tmp2.txt',mode='r')
    value_hum = f2.readline().split()
    f2.close()
    value_pm.pop()
    value_pm.pop()
    value_hum.pop()
    value_hum.pop()
    value_pm = list(map(float,value_pm))
    value_hum = list(map(float,value_hum))
    strs = list(range(0,4))
    strs[0] = pm10 + str(round(value_pm[0],2)) + prefix
    strs[1] = pm25 + str(round(value_pm[1],2)) + prefix
    strs[2] = hum + str(round(value_hum[0],2)) + "%"
    strs[3] = tem + str(round(value_hum[1],2)) + prefix2
    for _ in range(29):
        mylcd.lcd_display_string(strs[0],1)
        mylcd.lcd_display_string(strs[1],2)
        sleep(1)
        mylcd.lcd_clear()
        mylcd.lcd_display_string(strs[2],1)
        mylcd.lcd_display_string(strs[3],2)
        sleep(1)
        mylcd.lcd_clear()