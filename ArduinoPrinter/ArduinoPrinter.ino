#include "Printer.h"

#define TX_PIN 6 // Arduino transmit  YELLOW WIRE  labeled RX on printer
#define RX_PIN 5 // Arduino receive   GREEN WIRE   labeled TX on printer

#define LED_PIN 13

Printer printer(RX_PIN, TX_PIN);

//===============

void setup() {
  Serial.begin(115200);
  printer.begin(19200);
      
  pinMode(LED_PIN, OUTPUT);
  
  delay(1000);
  Serial.println("Arduino is ready.");
  flash();
  delay(1000);
}

//===============

void loop() {
  while (!Serial.available());
  Serial.print("Received: ");
  Serial.println(Serial.readString());

  flash();
  printer.print();
}

//===============

void flash() {
  digitalWrite(LED_PIN, HIGH);
  delay(200);
  digitalWrite(LED_PIN, LOW);
  delay(200);
  digitalWrite(LED_PIN, HIGH);
}
