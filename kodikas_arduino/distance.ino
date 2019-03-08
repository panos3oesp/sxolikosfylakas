#define sensor A0 // Sharp IR GP2Y0A41SK0F (4-30cm, analog)
#define sensor1 A1 // Sharp IR GP2Y0A41SK0F (4-30cm, analog)
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // start the serial port
}
void loop() {
  //  // put your main code here, to run repeatedly:
  float volts = analogRead(sensor) * 0.0048828125; // value from sensor * (5/1024)
  int distance = 13 * pow(volts, -1); // worked out from datasheet graph

  float volts1 = analogRead(sensor1) * 0.0048828125; // value from sensor1 * (5/1024)
  int distance1 = 13 * pow(volts1, -1); // worked out from datasheet graph

  delay(200); // slow down serial port
 if (distance <= 20 || distance1 <= 20 ) {
   Serial.print(String(distance)+","+String(distance1));   // print the distance
    
  } 
}
