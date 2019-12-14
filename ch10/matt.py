#-*-coding:utf-8-*-

import paho.mqtt.client as mqtt                    #Paho-MQTT 패키지 불러오기
from flask import Flask, render_template, request   #Flask 패키지 불러오기 
app = Flask(__name__)                            #Flask 모듈 불러오기

#matt 클라이언트를 생성하여 연결
mqttc=mqtt.Client()
mqttc.connect("localhost",1883, 60)
mqttc.loop_start()

# led 란 딕셔너리를 만듭니다. ‘name’과 ‘state’ 요소를 사용
led = {'name' : 'LED pin', 'state' : 'ON'}
  
# 웹서버의 URL 주소로 접근하면 아래의 main() 함수를 실행
@app.route("/")
def main():
   # led 딕셔너리를 templateData에 저장 
   templateData = {
      'led' : led
   }
   return render_template('main.html', **templateData)

# URL 주소 끝에 “/LED/<action>”을 붙여서 접근시에 action 값에 따라 동작
@app.route("/LED/<action>")
def action(action):

   # 만약에 action 값이 “on”과 같으면 mqtt 메시지를 토픽 “inTopic”에 “1”을 전송
   if action == "on":
      mqttc.publish("inTopic","1")
      led['state'] = "ON"
      message = "LED on.“
   # 만약에 action 값이 “off”과 같으면 mqtt 메시지를 토픽 “inTopic”에 “0”을 전송
   if action == "off":
      mqttc.publish("inTopic","0")
      led['state'] = "OFF"
      message = "LED off."

   templateData = {
      'message' : message,
      'led' : led
   }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=False)
