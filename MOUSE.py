
import mouse, sys
import time 
import serial

mouse.FAILSAFE=False
ArduinoSerial=serial.Serial('com3',9600)  #Specify the correct COM port
                           #delay of 1 second

while 1:
   data=str(ArduinoSerial.readline().decode('ascii')).replace("\r\n","")   #read the data
   if data[-1] == '1':                        # read the Status of SW
      mouse.click(button="left")
      print('yes')
      continue
   (x,y,z)=data.split(":")           # assigns to x,y and z
   (X,Y)=mouse.get_position()        #read the cursor's current position
   (x,y)=(int(x),int(y))                           #convert to int
   mouse.move(X-x,Y-y)           #move cursor to desired position
'''   if '1' in z:                        # read the Status of SW
      mouse.click(button="left")    # clicks left button
'''     