import requests
import base64

f = open("conf", "r")

pw = base64.b64decode(f.read()).decode('utf-8')

r = requests.get('https://accounts.kakao.com/login', auth=('junho85@gmail.com', pw))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)