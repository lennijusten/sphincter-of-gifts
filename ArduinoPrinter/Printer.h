#ifndef PRINTER_H
#define PRINTER_H

#include "Arduino.h"
#include "SoftwareSerial.h"
#include "Adafruit_Thermal.h"
#include "Ascii.h"

class Printer {
  public:
    Printer(int RX_PIN, int TX_PIN) : m_serial(RX_PIN, TX_PIN), m_printer(&m_serial) {}

    void begin(unsigned long baud_rate = 19200) {
      m_serial.begin(baud_rate);
      m_printer.begin();
    }

    void print(String date) {
      m_printer.justify('C');
      m_printer.setSize('M');
      m_printer.doubleHeightOn();
      m_printer.boldOn();
      
      m_printer.feed(3);

      m_printer.println(date);
      m_printer.setSize('S');
      
      m_printer.feed(1);
      
      m_printer.setSize('S');
      unsigned long idx = random(6);
      m_printer.println(ascii_art[idx]);
      
      idx = random(6);
      m_printer.println(ascii_art[idx]);
      
      m_printer.feed(1);

      m_printer.setSize('M');
      m_printer.println("FROM MY\nSPHINCTER\nTO YOUR\nMOUTH");
      
      m_printer.feed(1);
      
      m_printer.boldOff();
      m_printer.setSize('S');
      m_printer.println("Redeem for a Martian MargharET.");
      m_printer.feed(1);
      m_printer.println("10/13/23");
//      m_printer.println("Ticket ID: ");
//      m_printer.println(id);
      
      m_printer.setSize('L');
      m_printer.feed(8);
      
//      m_printer.sleep();
//      delay(500);
//      m_printer.wake();
//      m_printer.setDefault();
    }

  private:
    SoftwareSerial m_serial;
    Adafruit_Thermal m_printer;
};

#endif
