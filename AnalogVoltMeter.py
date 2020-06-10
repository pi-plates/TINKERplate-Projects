import piplates.TINKERplate as TINK
import time

TINK.setDEFAULTS(0)         #return all ports to their default states
TINK.setMODE(0,8,'servo')   #set Digital I/O port 1 to drive a servo
lLimit=12.0                 #The lower limit = 0 volts
hLimit=166.0                #The upper limit = 12 volts


while(True):
    analogIn=TINK.getADC(0,1)   #read analog channel 1
    #scale the data to an angle in the range of lLimit to hLimit
    angle=analogIn*(hLimit-lLimit)/12.0
    TINK.setSERVO(0,8,lLimit+angle) #set servo angle 
    time.sleep(.1)              #delay and repeat


        
