# BBGreat
This repository can be used to program the BB8-inspired device desribed here: http://poe.olin.edu/2018/poetential/

Dependencies for the ESP8266 WiFi chip code include the ESP8266WiFi library, the Adafruit MQTT library, and Wire.h. These are already included at the top of the script, but you may need to download the packages if they are not already on your computer.

For the Arduino code you will need: the Adafruit motorshield library and wire.h. Again, these are already included in the script, but you may need to download the specific packages.

Finally, when setting up your RasPi make sure that you run "sudo apt-get install mosquitto" in the RasPi command prompt to ensure you have the necessary software. If you have issues see this tutorial:https://www.hackster.io/ruchir1674/raspberry-pi-talking-to-esp8266-using-mqtt-ed9037. Then load the desired .py files onto your device. To run the face detection script you will need to load this xml file onto your device:https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
