#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다. (BMP180)
import bmpsensor
import time

# 온도, 압력, 고도 값을 읽어서 변수에 저장 
temp, pressure, altitude = bmpsensor.readBmp180()

# 측정값을 출력 
while True:
    print('Temp = {0:0.2f} *C'.format(temp))
    print('Pressure = {0:0.2f} Pa'.format(pressure))
    print('Altitude = {0:0.2f} m'.format(altitude))
    print("\n")
    time.sleep(2)
