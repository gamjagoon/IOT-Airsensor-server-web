import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()
pm10 = "pm10 "
pm25 = "pm25 "
prefix = "ug/m3"
while 1 :
    f = open('./tmp.txt',mode='r')
    value = f.readline().split()
    value.pop()
    value.pop()
    value = map(float,value)
    str1 = ""
    str2 = ""
    val1 = round(value[0],2)
    val2 = round(value[1],2)
    str1 = str1 + pm10 + str(round(val1,2)) + prefix
    str2 = str2 + pm25 + str(round(val2,2)) + prefix
    mylcd.lcd_display_string(str1,1)
    mylcd.lcd_display_string(str2,2)
    f.close()
    sleep(30)