import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(1)
    camera.capture('cos.jpg')
    camera.stop_preview()
