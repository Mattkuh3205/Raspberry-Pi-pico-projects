'''note, black/brown = ground, red = supply voltage, orange = control wire'''

import machine
import time
servoPin = 15
servo = machine.PWM(machine.Pin(servoPin))
servo.freq(50)



min_duty = 1802 #0
max_duty = 8000 #180




while True:
  
    servo.duty_u16(min_duty)
    time.sleep(1)
    
    
    servo.duty_u16(max_duty)
    time.sleep(1)
    
    
    servo.duty_u16(0)
    
    break;
    
    
    
    
  
   