char prevData = '0';  // store previous gesture

void setup()
{
  Serial.begin(9600);

  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0)
  {
    char data = Serial.read();

    // sirf update kare jab naya data aaye
    if (data != prevData)
    {
      prevData = data;

      // pehle sab LED OFF
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);

      // data ke hisab se LED ON
      if (data == '1') digitalWrite(8, HIGH);
      else if (data == '2') { digitalWrite(8, HIGH); digitalWrite(9, HIGH); }
      else if (data == '3') { digitalWrite(8, HIGH); digitalWrite(9, HIGH); digitalWrite(10, HIGH); }
      else if (data == '4') { digitalWrite(8, HIGH); digitalWrite(9, HIGH); digitalWrite(10, HIGH); digitalWrite(11, HIGH); }
    }
  }
}