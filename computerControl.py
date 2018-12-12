from imutils.object_detection import non_max_suppression
from imutils import paths
import imutils
from time import sleep
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import os

print("Booted. Starting controller.")

while True:
    message = "0,0"
    handle = raw_input("COM:")
    if len(handle) > 0:
        if handle == 'w':
            message = "35,35"
        elif handle == 'a':
            message = "0,30"
        elif handle == 'd':
            message = "30,0"
        elif handle == 's':
            message = "0,0"
    print(message)
    os.system('mosquitto_pub -h raspberrypi -t "/leds/esp8266" -m "' + message  + '"')

    if handle == 'q':
        break