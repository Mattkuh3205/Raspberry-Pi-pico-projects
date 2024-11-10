from machine import Pin
import time

p16 = Pin(16, Pin.OUT)
p17 = Pin(17, Pin.OUT)   
p18 = Pin(18, Pin.OUT)   
p19 = Pin(19, Pin.OUT)   


while True:
  
        print("Please enter a binary number: ")   
        user_input1 = input("")
        user_input2 = input("")
        user_input3 = input("")
        user_input4 = input("")
        print("Binary numbers: "+user_input1+user_input2+user_input3+user_input4)
        
        
       
        if user_input1 == "1":
            p16.on()
            print("Pin 1: on")
        elif user_input1 == "0":
            p16.off()    
            print("Pin 1: off")
    
      
        if user_input2 == "1":
            p17.on()
            print("Pin 2: on")
        elif user_input2 == "0":
            p17.off()    
            print("Pin 2: off")

     
        if user_input3 == "1":
            p18.on()
            print("Pin 3: on")
        elif user_input3 == "0":
            p18.off()    
            print("Pin 3: off")
        
        if user_input4 == "1":
            p19.on()
            print("Pin 4: on")
        elif user_input4 == "0":
            p19.off()  
            print("Pin 4: off")  
        
        time.sleep(1)
           
        p16.off()
        p17.off()
        p18.off()
        p19.off()
  
        break;
        
        
   
  