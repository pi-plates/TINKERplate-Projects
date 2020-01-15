import piplates.TINKERplate as TINK
import time

string0 = [0xFF,0xFF,0xFF]  #Create a single full white LED pattern
TINK.setDEFAULTS(0)         #set all Digital I/O ports to their default states
TINK.setMODE(0,1,'rgbled')  #set the mode of Digital I/O port 1 to RGB LED

while(True):                #start repeating loop
    ain=TINK.getADC(0,3)    #read the voltage on Analog Input channel 3
    k=(ain-0.3)/3.7         #subtract a 0.3V offset and scale result         
    if(k<0):
        k=0                 #clip lower limit to 0
    if(k>1):
        k=1                 #clip upper limit to 1
    print(ain)             #debug statement - uncomment to use
    string2=[(x * k) // 1 for x in string0] #scale the values in string0 from 0 through 255 
    print (string2)        #debug statement - uncomment to use
    #create the full, 8 channel RGB LED string:
    string1=string2+string2+string2+string2+string2+string2+string2+string2
    TINK.setRGBSTRING(0,1,string1)  #send eight LED claues to port 1    
    time.sleep(0.1)         #sleep 100msec before repeating