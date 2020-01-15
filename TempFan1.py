import piplates.TINKERplate as TINK
import time

tripTEMP=78     #this is the temperature we will operate around
hysteresis=1    #we will add a small amount of hysteresis to avoid chatter

threshold=tripTEMP-hysteresis   #the on/off threshold is the tripTEMP +/- the hysteresis 
fanON=True                  #initialize flag and..
TINK.relayON(0,1)           #turn on fan

TINK.setDEFAULTS(0)         #set all Digital I/O ports to their default states
TINK.setMODE(0,1,'temp')    #set the mode of Digital I/O port 1 to temperature

while(True):                #start loop
    temp=TINK.getTEMP(0,1)  #collect temperature data
    if (fanON):             
        if (temp<threshold):    #if on and temp is below threshold:
            fanON=False         #clear state
            TINK.relayOFF(0,1)  #turn off fan
            threshold=tripTEMP+hysteresis   #set high threshold
    else:
        if (temp>threshold):    #if off and temp is above threshold:
            fanON=True          #set state true
            TINK.relayON(0,1)   #turn on fan
            threshold=tripTEMP-hysteresis   #set low threshold   
    print ("Temperature:",temp,", Fan State:",fanON)
    time.sleep(1)           #sleep 1 sec then