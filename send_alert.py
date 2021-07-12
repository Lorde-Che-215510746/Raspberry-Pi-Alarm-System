import smtplib
from email.mime.text import MIMEText

#replace with with your credidentials
from_email_addr = 'bemaalert@gmail.com'
from_email_password = 'wardellprethan2001'
to_email_addr = 'che-lindsay-lorde@outlook.com'

#set email message
body = 'Motion was detected within room, check in on Bema'
msg = MIMEText(body)

#set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

#set email subject
msg['Subject'] = 'Bema Alert'

#connecting to server and sending email
#edit the following for provider's SMTP details
server = smtplib.SMTP('smtp.gmail.com', port = 587)
server.starttls()
server.login (from_email_addr, from_email_password)
server.sendmail (from_email_addr, to_email_addr, msg.as_string())
server.quit()
print('Email sent')

