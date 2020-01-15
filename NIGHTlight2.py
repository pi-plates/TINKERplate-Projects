import piplates.TINKERplate as TINK
import time

stringW = [0xFF,0xFF,0xFF]  #Create a single full white LED pattern
stringB = [0x0,0x0,0x0]     #Create a single full off LED pattern
TINK.setDEFAULTS(0)         #set all Digital I/O ports to their default states
TINK.setMODE(0,1,'rgbled')  #set the mode of Digital I/O port 1 to RGB LED

while(True):                #start repeating loop
    ain=TINK.getADC(0,3)    #read the voltage on Analog Input channel 3
    k=(ain-0.3)/3.7         #subtract a 0.3V offset and scale result         
    if(k<0):
        k=0                 #clip lower limit to 0
    if(k>1):
        k=1                 #clip upper limit to 1
    j=int(k*8.0+0.5)
    nlString=[]             #Create empty list
    for i in range(j):
        nlString=nlString+stringW   #populate 1st part of list with white LEDs
    for i in range(8-j):            
        nlString=nlString+stringB   #populate rest of list with OFF LEDs
    #print(j,nlString)      #debug statement - uncomment to use
    #print(ain)             #debug statement - uncomment to use
    TINK.setRGBSTRING(0,1,nlString)  #send eight LED values to port 1    
    time.sleep(0.1)         #sleep 100msec before repeating