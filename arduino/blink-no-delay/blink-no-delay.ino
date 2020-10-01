const int LED1 =  5;
const int LED2 =  6;

int ledState1 = 0;
int ledState2 = 0;

unsigned long previousMillis1 = 0;
unsigned long previousMillis2 = 0;

const long interval1 = 100;
const long interval2 = 500;

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  //LED1
  if (currentMillis - previousMillis1 >= interval1) {
    previousMillis1 = currentMillis;
    ledState1 ^=1;
    digitalWrite(LED1, ledState1);
  }

  //LED2
  if (currentMillis - previousMillis2 >= interval2) {
    previousMillis2 = currentMillis;
    ledState2 ^=1;
    digitalWrite(LED2, ledState2);
  }
}
