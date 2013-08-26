import smtplib
from email.mime.text import MIMEText

import smtplib
from email.mime.text import MIMEText

fromaddr = "justinhomesecure@gmail.com"
toaddrs = "justinrsmith88@gmail.com"
username = 'justinhomesecure@gmail.com'
password = "security2013"

msg="\r\n".join([
        "From: justinrsmith88@gmail.com",
        "To: justinrsmith88@gmail.com",
        "Subject: New Motion Detected",
        "",
        "New motion file has been created. Please follow link below to view."
        ])

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
print('sent triggered')
print('py3 dawg')
server.quit()

