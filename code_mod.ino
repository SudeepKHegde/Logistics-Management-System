#include <dht.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);
dht DHT;
#define DHT11_PIN 4
int v1pin = 2;
int v2pin = 3;

int v1Value;
int v2Value;

void setup() 
{
  Serial.begin(9600); 
  lcd.init();
  lcd.backlight();
  //Serial.println("Date & Time, Vib1  , Vib2  ,temp ,humidity %");
}
void loop() 
{
  delay(500);
  lcd.setCursor(2, 0); 
  lcd.print("LMS Active!"); 
  lcd.setCursor(2, 1); 
  lcd.print("HZ-05");
  v1Value = digitalRead(v1pin);
  //Serial.print("Vib-1 = ");
  //Serial.println(v1Value); 

  v2Value = digitalRead(v2pin);
  //Serial.print("Vib-2 = ");
  //Serial.println(v2Value); 

  int chk = DHT.read11(DHT11_PIN);
  //Serial.print("Temperature = ");
  //Serial.println(DHT.temperature);
  //Serial.print("Humidity = ");
  //Serial.println(DHT.humidity);


  Serial.print(",");
  Serial.print(v1Value);
  Serial.print(",");
  Serial.print(v2Value);
  Serial.print(",");
  Serial.print(DHT.temperature);
  Serial.print(",");
  Serial.println(DHT.humidity);
}
