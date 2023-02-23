#include <TinyGPS++.h>
#include <SoftwareSerial.h>

int RXPin = 2;
int TXPin = 3;

int GPSBaud = 9600;
TinyGPSPlus gps;
SoftwareSerial gpsSerial(RXPin, TXPin);

void setup()
{
  Serial.begin(9600); 
  gpsSerial.begin(GPSBaud);
}

void loop()
{
  while (gpsSerial.available() > 0)
    if (gps.encode(gpsSerial.read()))
      displayInfo();
      
  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println("No GPS detected");
    while(true);
  }
}

void displayInfo()
{
  if (gps.location.isValid())
  {
    Serial.print(",");
    Serial.print(gps.location.lat(), 6);
    Serial.print(",");
    Serial.print(gps.location.lng(), 6);
  
  }
  else
  {
    Serial.println("Location: Not Available");
  }
  
  Serial.println();
  delay(1000);
}
