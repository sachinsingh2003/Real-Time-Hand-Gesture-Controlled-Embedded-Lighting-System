# Hand Gesture Controlled LED System

## Overview
This project demonstrates a real-time hand gesture recognition system to control LEDs using computer vision and an embedded device. A webcam captures hand gestures, and a Python program detects the number of fingers using MediaPipe. The detected gesture is sent through serial communication to a microcontroller (Arduino/LPC2129), which controls LEDs accordingly.

## Features
- Real-time hand gesture detection
- Finger counting using computer vision
- Serial communication between PC and microcontroller
- LED control based on gestures
- Touchless hardware control

## Hardware Used
- Arduino Uno / LPC2129
- LEDs
- Resistors
- Jumper Wires
- USB Cable
- Webcam

## Software Used
- Python
- OpenCV
- MediaPipe
- Arduino IDE

## Working
1. The webcam captures live video of the hand.
2. MediaPipe detects hand landmarks and counts the number of fingers.
3. Python sends the finger count to the microcontroller via serial communication.
4. The microcontroller turns ON LEDs according to the received gesture.

## Example
| Fingers Detected | LED Output |
|------------------|-----------|
| 1 Finger | LED1 ON |
| 2 Fingers | LED1, LED2 ON |
| 3 Fingers | LED1, LED2, LED3 ON |
| 4 Fingers | LED1, LED2, LED3, LED4 ON |

## Author
Sachin Rawat
