# sending emails with python
from email.policy import SMTP
from http import server
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465

reciver = 'srajora102@gmail.com'
message = """\
Subject: Hi there!
    
This is a test message.
    """

sender = 'thebigbangtheory454@gmail.com'
password = input('Enter your password here:')

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    #send email
    server.sendmail(sender, reciver, message)




