// NeoPixel Ring simple sketch (c) 2013 Shae Erisson
// Released under the GPLv3 license to match the rest of the
// Adafruit NeoPixel library

#include <Adafruit_NeoPixel.h>

// Which pin on the Arduino is connected to the NeoPixels?
#define PIN 12

// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS 110

// LED Config
#define LED_BRIGHTNESS_MIN 0
#define LED_BRIGHTNESS_MAX 255
#define LED_BRIGHTNESS_DELTA 1
int brightness = LED_BRIGHTNESS_MIN + 1;
int brightness_delta = LED_BRIGHTNESS_DELTA;

#define DELAY 50

// When setting up the NeoPixel library, we tell it how many pixels,
// and which pin to use to send signals. Note that for older NeoPixel
// strips you might need to change the third parameter -- see the
// strandtest example for more information on possible values.
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

uint32_t PIXEL_GREEN = pixels.Color(0, 150, 0);
uint32_t PIXEL_PURPLE = pixels.Color(128, 0, 128);
uint32_t pixel_color = PIXEL_GREEN;

void setup() {
  pixels.begin();
}

void loop() {
  for(int i=0; i<NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixel_color);
  }
  
  pixels.setBrightness(brightness);
  if (brightness >= LED_BRIGHTNESS_MAX) {
    brightness_delta *= -1;
  } else if (brightness <= LED_BRIGHTNESS_MIN) {
    brightness_delta *= -1;
    pixel_color = pixel_color == PIXEL_GREEN ? PIXEL_PURPLE : PIXEL_GREEN;
  }
  brightness += brightness_delta;
  
  pixels.show();// Send the updated pixel colors to the hardware.
  delay(DELAY);
}
