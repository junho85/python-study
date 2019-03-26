import base64

encoded = base64.b64encode('안녕하세요'.encode('utf-8'))
print(encoded) # 7JWI64WV7ZWY7IS47JqU

decoded = base64.b64decode('7JWI64WV7ZWY7IS47JqU').decode('utf-8')
print(decoded) # 안녕하세요