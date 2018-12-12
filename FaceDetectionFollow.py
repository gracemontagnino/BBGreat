from imutils.object_detection import non_max_suppression
from imutils import paths
import imutils
from time import sleep
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import os

camera = PiCamera()
camera.resolution = (200,200)
camera.color_effects = (128,128)
rawCapture = PiRGBArray(camera,size=(200, 200))

print("Booted. Starting feed.")
last=False
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sleep(0.1)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = clahe.apply(image)
    image=cv2.flip(image,0)
    message = "0,0"

    if last==True:
        forward="25,25"
		os.system('mosquitto_pub -h raspberrypi -t "/leds/esp8266" -m "' + forward  + '"')
        last=False

    faces = face_cascade.detectMultiScale(image, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)
        off = ((float(x)+float(w)/2.0)/200.0 - 0.5)*50
        message = (str(-off) + "," + str(off))
        last=True

    print(message)
    os.system('mosquitto_pub -h raspberrypi -t "/leds/esp8266" -m "' + message  + '"')

    cv2.imshow("Output", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    rawCapture.truncate(0)