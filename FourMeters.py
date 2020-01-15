import METER as TINK  #import TIINKERplate module
import math  #import math module - needed for sine and pi
import time  #import the time module - needed for sleep

Mag=10
N=360
mColor=(255,255,0) #this tuple represents the color yellow
TINK.openMETER(4)  #create a panel meter with the default of a single line
TINK.setCOLOR(mColor)   #set meter color
TINK.setTITLE('Trigonometery Functions')    #Set meter title
while(True):  #Loop forever
    for i in range(N):   #do this 360 times
        TINK.setMETER(i,'degrees','Angle:',1)   #write angle to line 1
        val=math.sin(2*math.pi*i/360)           #calculate sine of angle
        TINK.setMETER(val,'','Sine:',2)         #write sine value to line 2
        val=math.cos(2*math.pi*i/360)           #calculate cosine of angle
        TINK.setMETER(val,'','Cosine:',3)       #write cosine value to line 3
        val=math.tan(2*math.pi*i/360)           #calculate tangent of angle
        TINK.setMETER(val,'','Tangent:',4)      #write tangent value to line 4        
        time.sleep(0.1)
    
    