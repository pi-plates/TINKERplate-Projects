import piplates.TINKERplate as TINK
import time
import traceback
#from decimal import Decimal

#set distance thresholds in inches
dMax=120.0
dClose=40.0
dGood=30.0
dDanger=20.0

stringR = [0xFF,0x0,0x0]    #Create a list of red LEDs patterns
for i in range(3):
    stringR=stringR+stringR
stringY = [0xFF,0xFF,0x00]  #Create a list of yellow LEDs patterns
for i in range(3):
    stringY=stringY+stringY
stringG = [0x0,0xFF,0x00]   #Create a list of green LEDs patterns
for i in range(3):
    stringG=stringG+stringG
stringO = [0x0,0x00,0x00]   #Create a list of off LEDs patterns
for i in range(3):
    stringO=stringO+stringO
    
TINK.setDEFAULTS(0)         #set all Digital I/O ports to their default states
TINK.setMODE(0,1,'rgbled')  #set the mode of Digital I/O port 1 to RGB LED
TINK.setMODE(0,5,'dout')    #set the mode of Digital I/O port 5 to digital output
TINK.setMODE(0,78,'range')  #set the mode of Digital I/O channel pair 78 to range

dist=0.0            #initialize global variables
bToggle=False
blink=False
alarm=False
zone=0
while(True):                #start repeating loop
    dist=TINK.getRANGEfast(0,78)
    #print(dist,zone)       #uncomment for debugging
    try:
        blink=False         #assume no blinking
        alarm=False         #assume no alarm
        if(dist > dMax):    #if measured distance is greater than dMax
            stringP=stringO #set LEDs to OFF
            zone=0
        elif(dist>dClose):
            stringP=stringG #set LEDs to green     
            zone=1           
        elif(dist>dGood):
            stringP=stringY #set LEDs to yellow           
            zone=2
        elif(dist>dDanger):
            stringP=stringR #set LEDs to red
            zone=3
        else:
            stringP=stringR #inside danger zone - set LEDs to red
            blink=True      #enable blinking   
            alarm=True      #enable alarm
            zone=4
        if((blink and bToggle) or (blink==False)):    
            TINK.setRGBSTRING(0,1,stringP)  #send eight LED values to port 1
        else:
            TINK.setRGBSTRING(0,1,stringO)  #send right off LEDs to port 1      
        if(alarm):
            TINK.setDOUT(0,5)       #turn on alarm if enabled
        else:
            TINK.clrDOUT(0,5)       #turn off alarm otherwise
        if (bToggle):               #toggle bToggle
            bToggle=False
        else:
            bToggle=True
    except:
        print("Stabilizing")
    time.sleep(0.2)         #sleep 100msec before repeating