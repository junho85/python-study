import smtplib

host = "mx1.hanmail.net"
port = 25

fromaddr = "abc@test.com"
toaddr = "junho85@daum.net"


smtp = smtplib.SMTP(host, port)
smtp.set_debuglevel(1)

msg = """Subject: this is test mail
from: abc@test.com

this is test mail
"""

smtp.sendmail(fromaddr, toaddr, msg)

smtp.quit()