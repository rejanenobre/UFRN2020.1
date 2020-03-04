bool data = 0;
int LED = 13;
char userInput;

void setup()
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop()
{
 if(Serial.available()>0)
 {
    userInput = Serial.read();
    if(userInput == '1')
    {
        data = !data;
        digitalWrite(LED, data);
    }
    Serial.println(data);
  }
}
