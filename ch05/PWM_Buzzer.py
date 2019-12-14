#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다. 
import RPi.GPIO as GPIO
import time

# 불필요한 warning 제거,  GPIO핀의 번호 모드 설정
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)

# GPIO 18번 핀을 출력으로 설정 
GPIO.setup(18, GPIO.OUT)
# PWM 인스턴스 p를 만들고  GPIO 18번을 PWM 핀으로 설정, 주파수  = 100Hz
p = GPIO.PWM(18, 100)  

# 4옥타브 도~시 , 5옥타브 도의 주파수 
Frq = [ 262, 294, 330, 349, 392, 440, 493, 523 ]
speed = 0.5 # 음과 음 사이 연주시간 설정 (0.5초)

p.start(10)  # PWM 시작 , 듀티사이클 10 (충분)

try:               
    while 1:   
        for fr in Frq:
            p.ChangeFrequency(fr)    #주파수를 fr로 변경
            time.sleep(speed)       #speed 초만큼 딜레이 (0.5s) 
             
except KeyboardInterrupt:       # 키보드 Ctrl+C 눌렀을때 예외발생 
    pass                       # 무한반복을 빠져나와 아래의 코드를 실행  
p.stop()                        # PWM을 종료
GPIO.cleanup()                 # GPIO 설정을 초기화 
