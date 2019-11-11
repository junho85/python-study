import chardet
import iconv_codecs

s = "안녕하세요"

# euc_data = '아름다운 한글'.encode('euc-kr')
# print(euc_data)

# 인코딩 알아내기
# print(chardet.detect(euc_data))

# print(s)
print(s.decode('utf-8').encode('euc-kr'))

# print(chardet.detect(s))
# print(str(s.decode('utf-8')))
