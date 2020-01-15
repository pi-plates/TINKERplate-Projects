import piplates.TINKERplate as TINK  #load TINKERplate module
import time                          #load time functions
d = '\u00b0'
TINK.setDEFAULTS(0)         #set all digital channel to defaults.
TINK.setMODE(0,1,'temp')    #Set channel 1 to read a temperature sensor
time.sleep(1)               #wait 1 second for stabilization
TINK.openMETER()            #Create a display meter on the screen
TINK.setTITLE('My Thermometer')
while(True):
    temp=TINK.getTEMP(0,1)
    TINK.setMETER(temp,d+'F','Channel 1:')
    time.sleep(1)
