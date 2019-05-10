/*
#-------------------------------------------------------------------------------
# Name:        CommunicationsManager
# Purpose:     Κλάση για αποστολή email 
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------
*/
#Set the pins of the sensors as constants
#define sensor0 A0 // Sharp IR GP2Y0A41SK0F (4-30cm, analog)
#define sensor1 A1 // Sharp IR GP2Y0A41SK0F (4-30cm, analog)
#define sensor2 A2 // Sharp IR GP2Y0A41SK0F (4-30cm, analog)
#define sensor3 A3 // Sharp IR GP2Y0A41SK0F (4-30cm, analog)

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // start the serial port
}



void loop() {
  //get analogue values for 4 distance sensors
  float distance0 = analogRead(sensor0);
  float distance1 = analogRead(sensor1);
  float distance2 = analogRead(sensor2);
  float distance3 = analogRead(sensor3);
  
  //if(Serial.available()){ // only send data back if data has been sent
  //if (distance0 <= 60 || distance1 <= 60 || distance2 <= 60 || distance3 <= 60 ) {
   Serial.println(String(distance0)+","+String(distance1)+","+String(distance2)+","+String(distance3));   // print the distance to the serial line
   delay(200); // slow down serial port
   Serial.flush(); //flush the data to sync
  //} 
  //}
  
}

