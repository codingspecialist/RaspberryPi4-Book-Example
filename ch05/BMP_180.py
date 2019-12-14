#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다. (BMP85/180)
import Adafruit_BMP.BMP085 as BMP085

# BMP180센서의 인스턴스 sensor 생성 
sensor = BMP085.BMP085()
# 온도, 압력, 고도 값을 읽어서 변수에 저장 
temp = sensor.read_temperature()
pressure = sensor.read_pressure()
altitude = sensor.read_altitude()
# 측정값을 출력 
print('Temp = {0:0.2f} *C'.format(temp))
print('Pressure = {0:0.2f} Pa'.format(pressure))
print('Altitude = {0:0.2f} m'.format(altitude))
