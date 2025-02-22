#define ESP32_RTOS  // Uncomment this line if you want to use the code with freertos only on the ESP32 \
                    // Has to be done before including "OTA.h"

#include "OTA.h"
#include <credentials.h>
#include "FS.h"
#include "SD.h"
#include "SPI.h"

const char *ssid = mySSID;
const char *password = myPASSWORD;

NetworkServer server(80);

String readFile(fs::FS &fs, String path) {
  Serial.println("Reading file: " + path);
  String out = "";

  File file = fs.open(path);
  if (!file) {
    Serial.println("Failed to open file for reading");
  } else {
    Serial.println("Read from file: ");
    while (file.available()) {
      char c = file.read();
      out += c;         // Append character to the String
      Serial.write(c);  // Output character to Serial
    }
    file.close();
  }
  return out;
}

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);  // set the LED pin mode

  delay(10);

  // We start by connecting to a WiFi network
  setupOTA("ESP32_HTML_Web_Server", mySSID, myPASSWORD);

  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();

  // SD Card Setup
  if (!SD.begin()) {
    Serial.println("Card Mount Failed");
    return;
  }
  uint8_t cardType = SD.cardType();

  if (cardType == CARD_NONE) {
    Serial.println("No SD card attached");
    return;
  }

  Serial.print("SD Card Type: ");
  if (cardType == CARD_MMC) {
    Serial.println("MMC");
  } else if (cardType == CARD_SD) {
    Serial.println("SDSC");
  } else if (cardType == CARD_SDHC) {
    Serial.println("SDHC");
  } else {
    Serial.println("UNKNOWN");
  }

  uint64_t cardSize = SD.cardSize() / (1024 * 1024);
  Serial.printf("SD Card Size: %lluMB\n", cardSize);
}

void loop() {
#ifdef defined(ESP32_RTOS) && defined(ESP32)
#else  // If you do not use FreeRTOS, you have to regulary call the handle method.
  ArduinoOTA.handle();
#endif

  NetworkClient client = server.accept();  // listen for incoming clients

  if (client) {                     // if you get a client,
    Serial.println("New Client.");  // print a message out the serial port
    String currentLine = "";        // make a String to hold incoming data from the client
    while (client.connected()) {    // loop while the client's connected
#ifdef defined(ESP32_RTOS) && defined(ESP32)
#else  // If you do not use FreeRTOS, you have to regulary call the handle method.
      ArduinoOTA.handle();
#endif
      if (client.available()) {  // if there's bytes to read from the client,
        char c = client.read();  // read a byte, then
        Serial.write(c);         // print it out the serial monitor
        if (c != '\r') {
          if (String(c).endsWith("\n")) {
            Serial.write("Newline");
          }
          currentLine += c;  // add it to the end of the currentLine
        }

        // that's the end of the client HTTP request, so send a response:
        if (currentLine.endsWith("\n\n")) {
          // Check to see if the client request was a GET.
          int getInd = currentLine.indexOf("GET ");
          int getHTTP = currentLine.indexOf(" HTTP");
          if (getInd != -1 && getHTTP != -1) {
            Serial.println(currentLine.substring(getInd + 4, getHTTP));
            String path = "/html" + currentLine.substring(getInd + 4, getHTTP) + "/index.html";
            Serial.println("Path: " + path);
            String html = readFile(SD, path);

            if (html != "") {
              digitalWrite(2, HIGH);  // Turns the LED on
              // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
              // and a content-type so the client knows what's coming, then a blank line:
              client.println("HTTP/1.1 200 OK");
              client.println("Content-type:text/html");
              client.println();

              // the content of the HTTP response follows the header:
              client.print(html);
            } else {
              digitalWrite(2, LOW);  // Turns the LED off
              // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
              // and a content-type so the client knows what's coming, then a blank line:
              client.println("HTTP/1.1 404 Not Found");
              client.println("Content-type:text/html");
              client.println();

              // the content of the HTTP response follows the header:
              client.print("404: Page not found.");
            }
          } else {
            digitalWrite(2, LOW);  // Turns the LED off
          }

          // The HTTP response ends with another blank line:
          client.println();

          // Clear the currentLine.
          currentLine = "";

          // break out of the while loop:
          break;
        }
      }
    }
    // close the connection:
    client.stop();
    Serial.println("Client Disconnected.");
  }
}
