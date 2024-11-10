from machine import Pin
import time

led = Pin("LED", Pin.OUT)

while True:
    led.off()
    time.sleep(.3)
    led.on()
    time.sleep(.3)
    led.off()
    time.sleep(.3)
    led.on()
    time.sleep(.3)
    led.off()
    time.sleep(.3)
    led.on()
    time.sleep(.3)
   

    led.off()
    time.sleep(.1)
    led.on()
    time.sleep(.1)
    led.off()
    time.sleep(.1)
    led.on()
    time.sleep(.1)
    led.off()
    time.sleep(.1)
    led.on()
    time.sleep(.1)
    led.off()