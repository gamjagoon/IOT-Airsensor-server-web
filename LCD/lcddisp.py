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
    f = open('./tmp.txt',mode='r')
    value = list(f.readline().split())
    value = value[0:2]
    print(value)
    f.close()
    f2 = open('./tmp2.txt',mode='r')
    value2 = list(f2.readline().split())
    value2 = value2[0:2]
    f2.close()
    val1 = round(float(value[0]),2)
    val2 = round(float(value[1]),2)
    str1 = pm10 + str(val1) + prefix
    str2 = pm25 + str(val2) + prefix
    str3 = "hum:" + value2[0] + "%"
    str4 = "tem:"+ value2[1] + "C"
    for i in range(15):
        mylcd.lcd_display_string(str1,1)
        mylcd.lcd_display_string(str2,2)
        sleep(2)
        mylcd.lcd_clear()
        mylcd.lcd_display_string(str3,1)
        mylcd.lcd_display_string(str4,2)
        sleep(2)
        mylcd.lcd_clear()


