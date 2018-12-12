#include <Adafruit_MotorShield.h>
#include <Wire.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *wheelRight = AFMS.getMotor(1);
Adafruit_DCMotor *wheelLeft = AFMS.getMotor(2);

String mspeeds = "";
int ls = 0;
int rs = 0;

void setup() {
  Wire.begin(8);
  Wire.onRequest(requestEvent);
  Wire.onReceive(receiveEvent);
  Serial.begin(115200);
  Serial.println("Started WiFi.");
  Serial.println("BB8 - Acquiring motor controls...");
  AFMS.begin();
  initWheels();
  Serial.println("Done.");
  tone(7, 1000, 500);
}

void requestEvent() {
  Wire.write("Connection live.");
}

void parseData() {
  Serial.println(mspeeds);
  int del = mspeeds.indexOf(',');
  ls = (mspeeds.substring(0, del)).toInt();
  rs = (mspeeds.substring(del+1, mspeeds.length())).toInt();
  Serial.print(ls);
  Serial.print(" ");
  Serial.println(rs);
}

void receiveEvent() {
  mspeeds = "";
  while (0 < Wire.available()) {
    mspeeds += (char)Wire.read();
  }
  parseData();
}

void initWheels() {
  wheelRight->setSpeed(150);
  wheelRight->run(FORWARD);
  wheelRight->run(RELEASE);
  wheelLeft->setSpeed(150);
  wheelLeft->run(FORWARD);
  wheelLeft->run(RELEASE);
}

void loop() {
  wheelLeft->setSpeed(abs(ls));
  wheelRight->setSpeed(abs(rs));
  if (ls <= 0) {
    wheelLeft->run(FORWARD);
  } else if (ls > 0) {
    wheelLeft->run(BACKWARD);
  }
  if (rs <= 0) {
    wheelRight->run(FORWARD);
  } else if (rs > 0) {
    wheelRight->run(BACKWARD);
  }
  delay(10);
}
