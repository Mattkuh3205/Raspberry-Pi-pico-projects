'''note, black/brown = ground, red = supply voltage, orange = control wire'''

import machine
import time
servoPin = 15
servo = machine.PWM(machine.Pin(servoPin))
servo.freq(50)

x = 2.99;
y = int(x)

min_duty = 1802 #0
max_duty = 8000 #180
half_duty = int(max_duty/1.6) #45
quarter_duty = int(min_duty*2) #90
tq_duty = int(quarter_duty*y)



while True:
  
    servo.duty_u16(min_duty)
    time.sleep(.4)
    
    
    servo.duty_u16(max_duty)
    time.sleep(.4)
    
    servo.duty_u16(tq_duty)
    time.sleep(.4)
    
    servo.duty_u16(half_duty)
    time.sleep(.4)
    
        
    servo.duty_u16(quarter_duty)
    time.sleep(.4)
    
    
    servo.duty_u16(min_duty)
    time.sleep(.4)
    
    
    
   
   
        
    
    #notes: need some sort of loop using PWM to control the sweeping using the 360 servo, 
    #ex: for int i = 0, i>= min range, i++, goes to position
    # next loop, for int i = 65535, i <= max range, i--, goes back
    
    
    
    
  
   