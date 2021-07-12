import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) #read output from PIR sensor
GPIO.setup(3, GPIO.OUT) #output for LED pin

while True:
    i = GPIO.input(11)
    if i == 0: #when output from PIR is low
        print ('no intruders'), i
        GPIO.output(3, 0)  #turn off LED
        time.sleep(0.1)
        
    elif i ==1: #when output from PIR is high
            print ('intruder detected'), i
            GPIO.output(3, 1) #turn on LED
            time.sleep(0.1)
