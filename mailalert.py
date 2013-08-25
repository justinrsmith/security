import smtplib
from email.mime.text import MIMEText

import smtplib
from email.mime.text import MIMEText

fromaddr = "justinrsmith88@gmail.com"
toaddrs = "justinrsmith88@gmail.com"
username = 'justinrsmith88@gmail.com'
password='messi13arsenal'

msg="\r\n".join([
        "From: justinrsmith88@gmail.com",
        "To: justinrsmith88@gmail.com",
        "Subject: just a message",
        "",
        "Why!"
        ])

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
print('sent triggered')
print('py3 dawg')
server.quit()

