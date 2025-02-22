#define ESP32_RTOS  // Uncomment this line if you want to use the code with freertos only on the ESP32
                    // Has to be done before including "OTA.h"

#include "OTA.h"
#include <credentials.h>

int brightness = 0;
int direction = 1;

void setup() {
  Serial.begin(115200);
  Serial.println("Booting");

  setupOTA("ESP32_Autonomous_Car", mySSID, myPASSWORD);
  // pinMode(26, OUTPUT);
  // pinMode(13, INPUT);
  ledcAttach(27, 5000, 8);
}

void loop() {
  #ifdef defined(ESP32_RTOS) && defined(ESP32)
  #else // If you do not use FreeRTOS, you have to regulary call the handle method.
    ArduinoOTA.handle();
  #endif
  // analogWrite(26, 0);
  // brightness += direction;

  // if (brightness == 0) {
  //   direction = 1;
  // } 
  // if (brightness == 255) {
  //   direction = -1;
  // }

  ledcWrite(27, brightness);
  delay(5);
}