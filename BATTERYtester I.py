import piplates.TINKERplate as TINK
import time

#create battery state thresholds
VL=1.2
VH=1.4

TINK.openMETER(1)   #Create a panel meter on the screen

#Change window title:
TINK.setTITLE("TINKERplate Battery Tester") 
#TINK.setCOLOR((255,0,0))   #start with red text

while(True):
    bat=TINK.getADC(0,1)            #read analog chanel 1
    if (bat >= VH):
        TINK.setCOLOR((0,255,0))    #show green text
        TINK.setMETER(bat,'Volts','GOOD',1) #indicate a GOOD battery
    if ((bat >= VL) and (bat < VH)):
        TINK.setCOLOR((255,255,0))  #show yellow text
        TINK.setMETER(bat,'Volts','OK',1)   #indicate an OK battery
    if (bat < VL):
        TINK.setCOLOR((255,0,0))    #show red text
        TINK.setMETER(bat,'Volts','BAD',1)  #indicate a BAD battery
    time.sleep(.5)                  #delay and repeat
