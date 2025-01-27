from machine import Pin
import time

## for this code, I want to work on interfacing push buttons instead of the pin pad

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(14, Pin.IN, Pin.PULL_DOWN)

button3 = Pin(14, Pin.IN, Pin.PULL_DOWN)

button4 = Pin(14, Pin.IN, Pin.PULL_DOWN)


while True:
    
    PW = input("Please input password: ")
    
    if PW == button1.value(0) and PW == button2.value(1) and PW == button3.value(1) and PW == button4.value(1):
        print("hello")
    
    
    break;