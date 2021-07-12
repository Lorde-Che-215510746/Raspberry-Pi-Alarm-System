import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
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
        time.sleep(0.2)
        
    elif i ==1: #when output from PIR is high
            from_email_addr = 'bemaalert@gmail.com'
            from_email_password = 'wardellprethan2001'
            to_email_addr = 'BemaAlert@outlook.com'
            
            body = 'Motion has been detected, check in on Bema'
            msg = MIMEText(body)
            
            msg['From'] = from_email_addr
            msg['To'] = to_email_addr
            
            msg['Subject'] = 'Bema Alert'
            
            server = smtplib.SMTP('smtp.gmail.com', port = 587)
            server.starttls()
            server.login (from_email_addr, from_email_password)
            server.sendmail (from_email_addr, to_email_addr, msg.as_string())
            server.quit()
            print('Email Sent')
            
            GPIO.output(3, 1) #turn on LED
            time.sleep(30)
