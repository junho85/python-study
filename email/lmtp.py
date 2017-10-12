import smtplib

host = "junho85.pe.kr"
port = 2525

fromaddr = "abc@test.com"
toaddr = "sometest@daum.net"

lmtp = smtplib.LMTP(host, port)
lmtp.set_debuglevel(1)

msg = """Subject: this is test mail
from: abc@test.com

this is test mail
"""

lmtp.sendmail(fromaddr, toaddr, msg)

lmtp.quit()