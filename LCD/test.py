import I2C_LCD_driver
import random
from time import *
mylcd = I2C_LCD_driver.lcd()
pm10 = "pm10 "
pm25 = "pm25 "
prefix = "ug/m^3"
while 1 :
    str1 = ""
    str2 = ""
    val1 = random.uniform(21,22)
    val2 = random.uniform(21,23)
    str1 = str1 + pm10 + str(round(val1,2)) + prefix
    str2 = str2 + pm25 + str(round(val2,2)) + prefix
    mylcd.lcd_display_string(str1,1)
    mylcd.lcd_display_string(str2,2)
    sleep(1)