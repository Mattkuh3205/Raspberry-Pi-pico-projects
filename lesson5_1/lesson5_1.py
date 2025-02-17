import machine
from time import sleep

potPin = 28
myPot = machine.ADC(potPin)


while True:
    potVal = myPot.read_u16()
    formula = (3.3/65106)*potVal - ((432*3.3)/65106) #formula for voltage (maxVolts / maxVal for binary)*potVal - (minVal*maxVolts)/maxVal for binary
    print(formula,"volts")
    sleep(.1)