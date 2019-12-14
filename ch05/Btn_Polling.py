#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다. 
import RPi.GPIO as GPIO 
import time

# 사용할 GPIO 핀의 번호를 선정합니다.
button_pin = 15
 
# 불필요한 warning 제거
GPIO.setwarnings(False) 
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM) 

# 버튼 핀의 입력설정 , PULL DOWN 설정 
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

while 1:  #무한반복 
    # 만약 버튼핀에 High(1) 신호가 들어오면, "Button pushed!" 을 출력합니다.
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button pushed!")    
    time.sleep(0.1)    # 0.1초 딜레이 
