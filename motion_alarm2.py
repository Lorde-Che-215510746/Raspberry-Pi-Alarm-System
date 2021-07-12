#try code form video here (intruder alert sensor)
from gpiozero import LED, Button, MotionSensor
from time import sleep
import smtplib
from email.mime.text import MIMEText

#Objects refer ti each LED, button, and pir sensor
led = LED(17)
pir = MotionSensor(20)
button = Button(16)

#create alarm state
Alarm_state = False

#set email login details
from_email_addr = 'bemaalert@gmail.com'
from_email_password = 'wardellprethan2001'
to_email_addr = 'che-lindsay-lorde@outlook.com'

#set email message
body = 'Motion was detected within room, check in on Bema'
msg = MIMEText(body)

#set email recipiants
msg['From'] = from_email_addr
msg['To'] = to_email_addr

#set email subject
msg['Subject'] = 'Bema Alert'

while True:
    
    if button.is_pressed:
        Alarm_state = True
        print('Alarm ON')
        
    if Alarm_state == True:
        led.on()
        if pir.motion_detected == True:
            print('motion detected')
            sleep(1)
            led.off()
            
            #connect to server and sending email
            server = smtplib.SMTP('smtp.gmail.com', port = 587)
            server.starttls()
            server.login(from_email_addr, from_email_password)
            server.sendmail(from_email_addr, to_email_addr, msg.as_string())
            server.quit()
            print('Email sent')
            Alarm_state = False


    
    

               
   
    
    
        
        
    
        
        
