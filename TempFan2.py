import piplates.TINKERplate as TINK
import time

d = '\u00b0'              #create the degree symbol

tripTEMP=78     #this is the temperature we will operate around
hysteresis=1    #we will add a small amount of hysteresis to avoid chatter

threshold=tripTEMP-hysteresis   #the on/off threshold is the tripTEMP +/- the hysteresis 
fanON=True                  #initialize flag and..
TINK.relayON(0,1)           #turn on fan
TINK.setDEFAULTS(0)         #set all Digital I/O ports to their default states
TINK.setMODE(0,1,'temp')    #set the mode of Digital I/O port 1 to temperature

TINK.openMETER(1)           #Create a display meter on the screen
TINK.setTITLE('TINKERplate Demo')
TINK.setCOLOR((255,0,0))       #Set meter text color to RED to indicate warm range

while(True):                #start loop
    temp=TINK.getTEMP(0,1)  #collect temperature data
    TINK.setMETER(temp,d+'F','Temperature:')
    if (fanON):             
        if (temp<threshold):    #if on and temp is below threshold:
            fanON=False         #clear state
            TINK.relayOFF(0,1)  #turn off fan
            threshold=tripTEMP+hysteresis   #set high threshold
            TINK.setCOLOR((0,0,255))           #Set meter text color to BLUE to indicate cool range
            print ("Temperature:",temp,", Fan Off")  #indicate the state change
    else:
        if (temp>threshold):    #if off and temp is above threshold:
            fanON=True          #set state true
            TINK.relayON(0,1)   #turn on fan
            threshold=tripTEMP-hysteresis   #set low threshold
            fanState='ON'
            TINK.setCOLOR((255,0,0))  #Set meter text color to RED to indicate warm range
            print ("Temperature:",temp,", Fan ON")  #indicate the state change
    TINK.setMETER(temp,d+'F','Temperature:',1)  
    time.sleep(1)           #sleep 1 sec then