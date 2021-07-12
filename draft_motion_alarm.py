#import libraries 
from gpiozero import LED, Button, MotionSensor
import smtplib
from email.mime.text import MIMEText
from signal import pause
 
#create objects to refer to each LED, the button, and the PIR sensor
led_status = LED (17)
led_triggered = LED (18)
button = Button (16)
pir = MotionSensor (20)


#control variabels
motion_sensor_status = False
email_sent = False
  
  
#arm or disarm the PIR sensor
def arm_motion_sensor ():
    global email_sent
    global motion_sensor_status
    if motion_sensor_status == True:
        motion_sensor_status = False
        led_status.off ()
        led_triggered.off ()
    else:
        motion_sensor_status = True
        email_sent = False
        led_status.on ()

            
#send email when motion is detected and the PIR sensor is armed
def send_email ():
    global email_sent
    global motion_sensor_status
    if (motion_sensor_status == True and email_sent == False):
        
        from_email_addr = 'myemail@gmail.com'
        from_email_password = 'password'
        to_email_addr = 'sumthin@outlook.com'
        
        body = 'Motion was detected within room, check in on Bema'
        msg = MIMEText(body)
        
        msg ['From'] = from_email_addr
        msg ['To'] = to_email_addr
        
        msg ['Subject'] = 'Bema Alert'
        
        server = smtplib.SMTP ('smtp.gmail.com', port = 587)
        server.starttls ()
        server.login (from_email_addr, from_email_password)
        server.sendmail (from_email_addr, to_email_addr, msg.as_string())
        server.quit()
        email_sent = True
        led_triggered.on ()
        print ('Email sent')
        
button.when_pressed = arm_motion_sensor
pir.when_motion = send_email
        

    
pause()
               
   
    
    
        
        
    
        
        
