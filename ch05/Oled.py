#-*-coding:utf-8-*-

# 필요한 라이브러리 불러오기
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import bmpsensor

# I2C 설정
i2c = board.I2C()  # uses board.SCL and board.SDA
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# 화면 초기화
oled.fill(0)
oled.show()

# 화면 이미지 객체 
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# 폰트 및 사이즈 설정
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)

# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = oled.height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# 온도, 압력, 고도 값을 읽어서 변수에 저장 
temp, pressure, altitude = bmpsensor.readBmp180()

while True:
	# 측정값을 출력 (터미널) 
	print('Temp = {0:0.2f} *C'.format(temp))
	print('Pressure = {0:0.2f} Pa'.format(pressure))
	print('Altitude = {0:0.2f} m'.format(altitude))
	# OLED에 화면 표시 내용 
	draw.text((x,top),   'Temp = {0:0.2f} *C'.format(temp), font=font, fill=255)
	draw.text((x,top+10), 'Pressure = {0:0.2f} Pa'.format(pressure),font=font, fill=255)
	draw.text((x,top+20),'Altitude = {0:0.2f} m'.format(altitude), font=font, fill=255)
	# 화면 표시 
	oled.image(image)
	oled.show()
	# 딜레이 시간 2초 
	time.sleep(2) 

