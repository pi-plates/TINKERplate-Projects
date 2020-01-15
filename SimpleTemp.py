import piplates.TINKERplate as TINK  #load TINKERplate module
import time                          #load time functions
d = '\u00b0'              #create the degree symbol
TINK.setMODE(0,1,'temp')  #setmode
while(True):              #loop forever
    t=TINK.getTEMP(0,1)   #fetch temperature
    #print to the console
    print('Time:',time.ctime(),' - Temperature is:',t,d+'F') #print to the console
    time.sleep(1)         #delay 1 second