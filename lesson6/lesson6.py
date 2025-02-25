#focus is on if statements, and how they're used in python
from machine import Pin

led = Pin("LED", Pin.OUT)

while True:
    cmd = input('What do you want the LED to be? ')
    print(cmd)
    
    if(cmd == 'on'):
        led.value(1)
    
    if(cmd == 'off'):
        led.value(0)
        
    

    if(cmd == 'x'):
        break;
    