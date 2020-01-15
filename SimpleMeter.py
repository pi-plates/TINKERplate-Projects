import piplates.TINKERplate as TINK  #import TIINKERplate module
import math  #import math module - needed for sine and pi
import time  #import the time module - needed for sleep

Mag=10
N=360
TINK.openMETER()  #create a panel meter with the gefault of a single line
while(True):  #Loop forever
    for i in range(N):   #do this 360 times
        val=Mag*math.sin(2*math.pi*i/360)
        TINK.setMETER(val,'volts','Sine Data:')
        time.sleep(0.05)
    
    