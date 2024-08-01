#define VCC 3.3

#define THERMO_offset 53
#define THERMO_1 54
#define THERMO_2 55
#define THERMO_3 56
#define THERMO_4 57

#define HEATER_offset 47
#define HEATER_1 48
#define HEATER_2 49
#define HEATER_3 50
#define HEATER_4 51

void setup() {
  // Initialize the serial communication at 9600 baud rate
  Serial.begin(9600);

  pinMode(HEATER_1,OUTPUT);
  pinMode(HEATER_2,OUTPUT);
  pinMode(HEATER_3,OUTPUT);
  pinMode(HEATER_4,OUTPUT);

  pinMode(THERMO_1,INPUT);
  pinMode(THERMO_2,INPUT);
  pinMode(THERMO_3,INPUT);
  pinMode(THERMO_4,INPUT);
}

void loop() {
  // Array to store the voltage readings
  float voltages[4];
  int resistance[4];
  int thresholds[4] = {15000, 12750,10500,8700};
  int correction = 10000;
  bool heaters[4] = {0,0,0,0};
  
  // Read the voltage on A0 to A3 and store in the array
  for (int i = 0; i < 4; i++) {
    int sensorValue = analogRead(A0 + i);
    voltages[i] = sensorValue * (VCC / 1023.0);
    resistance[i] = (voltages[i] * 10000) / (VCC - voltages[i]);
  }
  
  // Print the voltages to the Serial Monitor on the same line
  Serial.print("Voltages: | ");
  for (int i = 0; i < 4; i++) {
    Serial.print(i);
    Serial.print(": ");
    Serial.print(voltages[i]);
    if (i < 3) {
      Serial.print(" | ");
    }
  }
  Serial.println();
  Serial.print("Resistances: | ");
  for (int i = 0; i < 4; i++) {
    Serial.print(i);
    Serial.print(": ");
    Serial.print(resistance[i]);
    if (i < 3) {
      Serial.print(" | ");
    }
  }
  Serial.println();
  
   for (int i = 0; i < 4; i++) {
    if((resistance[i] + correction) < thresholds[i]){
      digitalWrite(HEATER_offset+i,LOW);
      Serial.print(i);
      Serial.print(" : Too hot! ");
      heaters[i] = 0;
    }
    else{
      digitalWrite(HEATER_offset+i,HIGH);
      heaters[i] = 1;
    }
   }
    Serial.println();
    Serial.print("Heaters: ");
    for (int i = 0; i < 4; i++) {
    Serial.print(i);
    Serial.print(": ");
    Serial.print(heaters[i]);
    if (i < 3) {
      Serial.print(" | ");
    }
  }
  Serial.println();
}  
