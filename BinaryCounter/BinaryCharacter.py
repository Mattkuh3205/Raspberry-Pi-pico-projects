from machine import Pin
import time

p16 = Pin(16, Pin.OUT)
p17 = Pin(17, Pin.OUT)   
p18 = Pin(18, Pin.OUT)   
p19 = Pin(19, Pin.OUT)   
p20 = Pin(20, Pin.OUT)
p21 = Pin(21, Pin.OUT)
p22 = Pin(22, Pin.OUT)
p26 = Pin(26, Pin.OUT)

while True:
        
        bin_a =  ("01100001");
        bin_b  = ("01100010");
        bin_c  = ("01100011");
        bin_d  = ("01100100");
        bin_e  = ("01100101");
        bin_f  = ("01100110");
        bin_g  = ("01100111");
        bin_h  = ("01101000");
        bin_i  = ("01101001");
        bin_j  = ("01101010");
        bin_k  = ("01101011");
        bin_l  = ("01101100");
        bin_m  = ("01101101");
        bin_n  = ("01101110");
        bin_o  = ("01101111");
        bin_p  = ("01110000");
        bin_q  = ("01110001");
        bin_r  = ("01110010");
        bin_s  = ("01110011");
        bin_t  = ("01110100");
        bin_u  = ("01110101");
        bin_v  = ("01110110");
        bin_w  = ("01110111");
        bin_x  = ("01111000");
        bin_y =  ("01111001");
        bin_z  = ("01111010");


        
        
  
        print("Please enter a binary number: ")   
        
        user_input1, user_input2, user_input3, user_input4, user_input5, user_input6, user_input7, user_input8 = input('')
        
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
            
        if user_input5 == "1":
            p20.on()
            print("Pin 5: on")
        elif user_input5 == "0":
            p20.off()    
            print("Pin 5: off")
    
      
        if user_input6 == "1":
            p21.on()
            print("Pin 6: on")
        elif user_input6 == "0":
            p21.off()    
            print("Pin 6: off")

     
        if user_input7 == "1":
            p22.on()
            print("Pin 7: on")
        elif user_input7 == "0":
            p22.off()    
            print("Pin 7: off")
        
        if user_input8 == "1":
            p26.on()
            print("Pin 8: on")
        elif user_input8 == "0":
            p26.off()  
            print("Pin 8: off")  

      

        time.sleep(1)
           
        p16.off()
        p17.off()
        p18.off()
        p19.off()
        p20.off()
        p21.off()
        p22.off()
        p26.off()
        
       
        fullInput = user_input1+user_input2+user_input3+user_input4+user_input5+user_input6+user_input7+user_input8
        if fullInput == bin_a:
            print("Binary: "+bin_a)
            print("Character: a")
        elif fullInput == bin_b:
            print("Binary: "+bin_b)
            print("Character: b")
        elif fullInput == bin_c:
            print("Binary: "+bin_c)
            print("Character: c")
        elif fullInput == bin_d:
            print("Binary: "+bin_d)
            print("Character: d")
        elif fullInput == bin_e:
            print("Binary: "+bin_e)
            print("Character: e")
        elif fullInput == bin_f:
            print("Binary: "+bin_f)
            print("Character: f")
        elif fullInput == bin_g:
            print("Binary: "+bin_g)
            print("Character: g")
        elif fullInput == bin_h:
            print("Binary: "+bin_h)
            print("Character: h")
        elif fullInput == bin_i:
            print("Binary: "+bin_i)
            print("Character: i")
        elif fullInput == bin_i:
            print("Binary: "+bin_i)
            print("Character: i")
        elif fullInput == bin_j:
            print("Binary: "+bin_j)
            print("Character: j")
        elif fullInput == bin_k:
            print("Binary: "+bin_k)
            print("Character: k")
        elif fullInput == bin_l:
            print("Binary: "+bin_l)
            print("Character: l")
        elif fullInput == bin_m:
            print("Binary: "+bin_m)
            print("Character: m")
        elif fullInput == bin_n:
            print("Binary: "+bin_n)
            print("Character: n")
        elif fullInput == bin_o:
            print("Binary: "+bin_o)
            print("Character: o")
        elif fullInput == bin_p:
            print("Binary: "+bin_p)
            print("Character: p")
        elif fullInput == bin_q:
            print("Binary: "+bin_q)
            print("Character: q")
        elif fullInput == bin_r:
            print("Binary: "+bin_r)
            print("Character: r")
        elif fullInput == bin_s:
            print("Binary: "+bin_s)
            print("Character: s")
        elif fullInput == bin_t:
            print("Binary: "+bin_t)
            print("Character: t")
        elif fullInput == bin_u:
            print("Binary: "+bin_u)
            print("Character: u")
        elif fullInput == bin_v:
            print("Binary: "+bin_v)
            print("Character: v")
        elif fullInput == bin_w:
            print("Binary: "+bin_w)
            print("Character: w")
        elif fullInput == bin_x:
            print("Binary: "+bin_x)
            print("Character: x")
        elif fullInput == bin_y:
            print("Binary: "+bin_y)
            print("Character: y")
        elif fullInput == bin_z:
            print("Binary: "+bin_z)
            print("Character: z")

        break;