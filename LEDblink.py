import piplates.TINKERplate as TINK
import time

for i in range(100): #Repeat this loop 100 times
	TINK.clrLED(0,0) #LED off
	time.sleep(0.05) #sleep for 50msec
	TINK.setLED(0,0) #LED on time.sleep(0.05) #sleep for 50msec
	
print ("I'm all blinked out!")
