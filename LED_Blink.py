impor RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT) #defines pin 3 as output pin

while True: 
    GPIO.output(3, 1) #outputs digital high signal 5V on pin 3
    time.sleep(1) #time delay of 1 sec
    
    GPIO.output(3,0) #Outputs digital low signal 0V on pin 3
    time.sleep(1) #time delay of 1 sec