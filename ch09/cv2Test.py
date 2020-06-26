#coding:utf-8
import cv2
cam = cv2.VideoCapture(0)

#FPS setting = speed up
cam.set(cv2.CAP_PROP_FPS, 7)

while True:
    ret,img = cam.read()
    #print(ret) #True, False
    cv2.imshow('Video Capture', img)
    key = cv2.waitKey(10)
    print("key : " + str(key))
    #space bar = 1048608
    #print(key)
    #ord = CHR -> ASCII
    #chr =  ASCII -> CHR

    if key != -1:
        if key == 32:
            print("cature : " + str(key))
            cv2.imwrite('capture.jpg',img)
        else:
            print("fail : " + str(key))
            break
