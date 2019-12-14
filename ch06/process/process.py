from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

LED = 8
GPIO.setmode(GPIO.BOARD) #BOARD는 커넥터 pin번호 사용
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route("/led/<state>")
def led(state):
    if(state == "on"):
        GPIO.output(LED, GPIO.HIGH)
        return "LED ON"
    elif(state == "off"):
        GPIO.output(LED, GPIO.LOW)
        return "LED OFF"
    else:
        return "error"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")