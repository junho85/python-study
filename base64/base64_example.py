import base64

encoded = base64.b64encode('안녕하세요'.encode('utf-8'))
print(encoded) # 7JWI64WV7ZWY7IS47JqU

decoded = base64.b64decode('7JWI64WV7ZWY7IS47JqU').decode('utf-8')
print(decoded) # 안녕하세요

encoded = base64.b64encode('데스크탑_MAC_Address.txt'.encode('utf-8'))
print(encoded) # 642w7Iqk7YGs7YORX01BQ19BZGRyZXNzLnR4dA==

encoded = base64.b64encode('데스크탑_MAC_Address.txt'.encode('euc-kr'))
print(encoded) # taW9usWpxb5fTUFDX0FkZHJlc3MudHh0
print(base64.b64decode('taW9usWpxb5fTUFDX0FkZHJlc3MudHh0').decode('euc-kr')) # 데스크탑_MAC_Address.txt
