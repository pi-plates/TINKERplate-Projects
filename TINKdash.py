import piplates.TINKERplate as TINK
import time
import subprocess
from guizero import App, Box, Text, ButtonGroup, Picture, Slider, PushButton

def dashboard():        #update all periodic ana log and digital inputs
    adc1=TINK.getADC(0,1)   #\
    adc2=TINK.getADC(0,2)   # \___Read all analog inputs
    adc3=TINK.getADC(0,3)   # /
    adc4=TINK.getADC(0,4)   #/
    adcVal1.value=str("{:2.3f}".format(TINK.getADC(0,1)))   #\
    adcVal2.value=str("{:2.3f}".format(TINK.getADC(0,2)))   # \_Format analog values update data on screen   
    adcVal3.value=str("{:2.3f}".format(TINK.getADC(0,3)))   # /
    adcVal4.value=str("{:2.3f}".format(TINK.getADC(0,4)))   #/      
    dinVal1.value=str(TINK.getDIN(0,1))   #\
    dinVal2.value=str(TINK.getDIN(0,2))   # \___Read all digital inputs and update data on screen
    dinVal3.value=str(TINK.getDIN(0,3))   # /
    dinVal4.value=str(TINK.getDIN(0,4))   #/
    
    
def relay1Change(): #Callback function for Relay 1
    if(rly1Cntl.value=='CLOSE'):
        TINK.relayOFF(0,1)
    else:
        TINK.relayON(0,1)
    
def relay2Change(): #Callback function for Relay 2
    if(rly1Cnt2.value=='CLOSE'):
        TINK.relayOFF(0,2)
    else:
        TINK.relayON(0,2)

def ledChange():    #Callback function for on board LED
    if(ledCntl.value=='ON'):
        TINK.setLED(0,0)
    else:
        TINK.clrLED(0,0)

def openRef():  #callback function to open commad reference
    code=subprocess.call(["qpdfview","TINKERplate Command Reference.pdf"])
        
def pwm5Change():  #Callback function for pwm output 5
    val=int(dpwm5.value)
    TINK.setPWM(0,5,val)

def pwm6Change():  #Callback function for pwm output 6
    val=int(dpwm6.value)
    TINK.setPWM(0,6,val)     
    
def dout7Change():  #Callback function for digital output 7
    if(doutCnt7.value=='SET'):
        TINK.setDOUT(0,7)
    else:
        TINK.clrDOUT(0,7)
        
def dout8Change():  #Callback function for digital output 8
    if(doutCnt8.value=='SET'):
        TINK.setDOUT(0,8)
    else:
        TINK.clrDOUT(0,8)      
       
#Initialize TINKERplate Digital I/O lines
TINK.RESET(0)
time.sleep(0.5)
TINK.setMODE(0,1,'din')
TINK.setMODE(0,2,'din')
TINK.setMODE(0,3,'din')
TINK.setMODE(0,4,'din')
TINK.setMODE(0,5,'pwm')
TINK.setMODE(0,6,'pwm')
TINK.setMODE(0,7,'dout')
TINK.setMODE(0,8,'dout')

#Define the overall characteristics of our dashboard including size and background color
app = App(title="TINKERplate Dashboard",bg="white",layout="grid",width=750,height=360)
dashTitle=Text(app,text= "",width="fill",grid=[0,0,5,1])

#insert the callout image on the left side
callOuts=Picture(app, grid=[0,1,3,3], image="Pinouts.jpg",width=400,height=271)

#Create two "result" boxes to contain the widgets
rBox=Box(app, width="fill", height="fill", align="top", border=1,grid=[4,1])
r2Box=Box(app, width="fill", height="fill", align="top", border=1,grid=[5,1])

#Create and populate the Analog to Digital data box - we use the Text widget here
adc_box=Box(rBox, width="fill", height="fill", align="top", border=1)
adcTitle=Text(adc_box, text="Analog Inputs", align="top",)
adc_val_box=Box(adc_box, width="fill", align="bottom", border=1,layout="grid")
adcChan=Text(adc_val_box, width="fill", text="Channel ",grid=[0,0])
adcVal=Text(adc_val_box, width="fill", text="Voltage",grid=[1,0])
adcL1=Text(adc_val_box, width="fill", text="1:",grid=[0,1])
adcL2=Text(adc_val_box, width="fill", text="2:",grid=[0,2])
adcL3=Text(adc_val_box, width="fill", text="3:",grid=[0,3])
adcL4=Text(adc_val_box, width="fill", text="4:",grid=[0,4])
adcVal1 = Text(adc_val_box, width="fill", text="0",grid=[1,1])
adcVal2 = Text(adc_val_box, width="fill", text="0",grid=[1,2])
adcVal3 = Text(adc_val_box, width="fill", text="0",grid=[1,3])
adcVal4 = Text(adc_val_box, width="fill", text="0",grid=[1,4])

#Create and populate the Relay box - we use the ButtonGroup widget here
relay_box=Box(rBox, width="fill", height="fill", border=1,layout="grid")
relayTitle=Text(relay_box, text="Relay Control",grid=[0,0],width="fill")
rlyCntl_box=Box(relay_box,layout="grid",border=0,grid=[0,1])
rly1Label=Text(rlyCntl_box,text='1:',grid=[0,0])
rly2Label=Text(rlyCntl_box,text='2:',grid=[0,1])
rly1Cntl=ButtonGroup(rlyCntl_box, command=relay1Change, options=["OPEN", "CLOSE"], selected="OPEN",horizontal=True,grid=[1,0])
rly1Cnt2=ButtonGroup(rlyCntl_box, command=relay2Change, options=["OPEN", "CLOSE"], selected="OPEN",horizontal=True,grid=[1,1])

#Create and populate the LED box - we use the ButtonGroup widget here
led_box=Box(rBox,width="fill", height="fill", border=1,layout="grid")
ledLabel=Text(led_box,text="LED:",grid=[0,0])
ledCntl=ButtonGroup(led_box, command=ledChange, options=["ON", "OFF"], selected="ON",horizontal=True,grid=[1,0]) 

#Create and populate the button box - we use the PushButton widget here
butt_box=Box(rBox,width="fill", height="fill", border=0)
cmdrefButton=PushButton(butt_box, width="fill", text="Command Reference", command=openRef)
cmdrefButton.text_color="#008000"

#Create and populate the DIO box
dio_box=Box(r2Box,width="fill", height="fill", border=1)
dioTitle=Text(dio_box,text="Digital I/O",align="top")

#Digital input setup for channels 1-4. This section relies on the Text widget
din_box=Box(dio_box,width="fill", border=1,layout="grid")
din_Title0=Text(din_box, text='   Basic Inputs',grid=[0,0,2,1],width="fill")
dinLabel1=Text(din_box, text='1:',width="fill",grid=[0,1])
dinLabel2=Text(din_box, text='2:',width="fill",grid=[0,2])
dinLabel3=Text(din_box, text='3:',width="fill",grid=[0,3])
dinLabel4=Text(din_box, text='4:',width="fill",grid=[0,4])
dinVal1=Text(din_box, text='1',width="fill",grid=[1,1])
dinVal2=Text(din_box, text='1',width="fill",grid=[1,2])
dinVal3=Text(din_box, text='1',width="fill",grid=[1,3])
dinVal4=Text(din_box, text='1',width="fill",grid=[1,4])

#PWM controls for channels 5 and 6 - we take advantage of the Slider widget here.
pwm_box=Box(dio_box,width="fill",border=1,layout="grid")
pwm_Title=Text(pwm_box, text='PWM Outputs',grid=[0,0,2,1],width="fill")
doutLabel5=Text(pwm_box, text='5:',width="fill",grid=[0,1])
doutLabel6=Text(pwm_box, text='6:',width="fill",grid=[0,2])
dpwm5=Slider(pwm_box,command=pwm5Change,grid=[1,1])
dpwm6=Slider(pwm_box,command=pwm6Change,grid=[1,2])

# Digital output controls for channels 7 and 8 - we again use the ButtonGroup widget here
dout_box=Box(dio_box,width="fill",border=1, align="bottom", layout="grid")
dout_Title=Text(dout_box, text='Basic Outputs',grid=[0,0,2,1],width="fill")
doutLabel7=Text(dout_box, text='7:',width="fill",grid=[0,1])
doutLabel8=Text(dout_box, text='8:',width="fill",grid=[0,2])
doutCnt7=ButtonGroup(dout_box, command=dout7Change, options=["SET", "CLEAR"], selected="CLEAR",horizontal=True,grid=[1,1])
doutCnt8=ButtonGroup(dout_box, command=dout8Change, options=["SET", "CLEAR"], selected="CLEAR",horizontal=True,grid=[1,2])


adcVal1.repeat(500,dashboard) #Use label as a timer to update inputs every 500mSec.
app.display()   #Launch and display our guizero-based dashboard.