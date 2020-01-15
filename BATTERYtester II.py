import piplates.TINKERplate as TINK
import time

#create battery state thresholds
VL=1.2
VH=1.4

TINK.setDEFAULTS(0)
TINK.setMODE(0,1,'rgbled')  #set Digital I/O port to display Neopixels

red=[255,0,0]   #define the red color mix
yel=[255,255,0] #define the yellow color mix
grn=[0,255,0]   #define the green color mix
off=[0,0,0]     #define an off LED
blank=off+off+off+off+off+off+off+off   #create a set of OFF LEDs
strip=red+red+red+red+yel+yel+grn+grn   #create the battery status lights
while(True):
    bat=TINK.getADC(0,1)            #read analog channel 1
    #scale the data to an integer in the range of 0 through 7
    temp=bat-0.8    #we will only look at the range from 0.8 volts to 1.6
    if (temp<0):
        index=0     #if the measured voltage is negative, set index to 0
    else:           #otherwise, convert the voltage to a list index
        index=int(temp*10)
        if (index>7):   #limit the maximum index to 7
            index=7
    batstrip=strip[0:3*(index+1)]+blank[0:3*(8-index)]  #assembled string
    TINK.setRGBSTRING(0,1,batstrip) #send string data to TINKERplate
    time.sleep(.5)                  #delay and repeat
