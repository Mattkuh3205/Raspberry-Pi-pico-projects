from machine import Pin
from time import sleep
""" 
pin assignments
"""

pin1 = Pin(15, Pin.OUT)
pin2 = Pin(14, Pin.OUT)
pin3 = Pin(13, Pin.OUT)
pin4 = Pin(12, Pin.OUT)



#binary order: bottom to top, 0,1,2,3,4 etc...
#4 bit binary (base 2) representation of decimal numbers (base 10)

#note: can have more numbers by expanding to 8 bits (1 byte) with 4 more pins/leds 2^8 (256 different numbers)


while True:
    
    #0
    pin1.value(0)
    pin2.value(0)
    pin3.value(0)
    pin4.value(0)
    sleep(.5)
    
    #1
    pin1.value(0)
    pin2.value(0)
    pin3.value(0)
    pin4.value(1)
    sleep(.5)
    
    #2
    pin1.value(0)
    pin2.value(0)
    pin3.value(1)
    pin4.value(0)
    sleep(.5)

    #3
    pin1.value(0)
    pin2.value(0)
    pin3.value(1)
    pin4.value(1)
    sleep(.5)
    
    #4
    pin1.value(0)
    pin2.value(1)
    pin3.value(0)
    pin4.value(0)
    sleep(.5)
    
    #5
    pin1.value(0)
    pin2.value(1)
    pin3.value(0)
    pin4.value(1)
    sleep(.5)
    
    #6
    pin1.value(0)
    pin2.value(1)
    pin3.value(1)
    pin4.value(0)
    sleep(.5)
    
    #7
    pin1.value(0)
    pin2.value(1)
    pin3.value(1)
    pin4.value(1)
    sleep(.5)
    
    #8
    pin1.value(1)
    pin2.value(0)
    pin3.value(0)
    pin4.value(0)
    sleep(.5)
    
    #9
    
    pin1.value(1)
    pin2.value(0)
    pin3.value(0)
    pin4.value(1)
    sleep(.5)
    
    #10
    
    pin1.value(1)
    pin2.value(0)
    pin3.value(1)
    pin4.value(0)
    sleep(.5)
    
    #11
    
    pin1.value(1)
    pin2.value(0)
    pin3.value(1)
    pin4.value(1)
    sleep(.5)
    
    #12
    pin1.value(1)
    pin2.value(1)
    pin3.value(0)
    pin4.value(0)
    
    #13
    pin1.value(1)
    pin2.value(1)
    pin3.value(0)
    pin4.value(1)
    
    #14
    pin1.value(1)
    pin2.value(1)
    pin3.value(1)
    pin4.value(0)
    
    #15
    pin1.value(1)
    pin2.value(1)
    pin3.value(1)
    pin4.value(1)
    
    
    pin1.value(0)
    pin2.value(0)
    pin3.value(0)
    pin4.value(0)
    
    
    #this basically acts as the end of the sequence, and stops the code after we reach the max amount of numbers we can represent in a 4 bit string
    break;

    
    
