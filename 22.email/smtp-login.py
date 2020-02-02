import smtplib
from email.mime.text import MIMEText

from_address = 'junho85@daum.net'
to_address = 'junho85@daum.net'

# smtp = smtplib.SMTP('smtp.daum.net', 587)
smtp = smtplib.SMTP_SSL('smtp.daum.net', 465)
# smtp.ehlo()
# smtp.starttls()
smtp.login('junho85', 'ㄴㄴㅁㄴ')

msg = MIMEText('테스트 메시지')
msg['Subject'] = '테스트 제목'
msg['To'] = to_address
smtp.sendmail(from_address, to_address, msg.as_string())

smtp.quit()