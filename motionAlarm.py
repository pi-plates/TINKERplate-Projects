import piplates.TINKERplate as TINK
import time

TINK.setDEFAULTS(0)         #initialize Digital I/O ports
TINK.setMODE(0,2,'din')     #set port 2 as an input for the motion sensor
TINK.setMODE(0,3,'dout')    #set port 3 as an output for the siren


while(True):
    motion=TINK.getDIN(0,2) #read motion sensor status
    if(motion==1):          #if motion detected
        TINK.relayON(0,1)       #turn on lamp
        TINK.setDOUT(0,3)       #turn on siren
    else:                   #if no motion
        TINK.relayOFF(0,1)      #turn off lamp
        TINK.clrDOUT(0,3)       #turn off siren
    time.sleep(0.1)         #wait 100msec and repeat
    