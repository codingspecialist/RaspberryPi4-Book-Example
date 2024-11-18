from picamera2 import Picamera2, Preview
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start_and_record_video("cos.h264", duration=5)