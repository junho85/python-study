# urllib.parse 모듈에서 quote와 urlparse 함수를 임포트
from urllib.parse import urlparse

# URL을 파싱하여 각 구성 요소로 분해
parsed_url = urlparse("https://junho85.pe.kr/1234")
print(parsed_url)  # 파싱된 URL의 전체 구조 출력

# netloc(네트워크 위치) 부분 추출
print(parsed_url.netloc)  # junho85.pe.kr

# netloc을 점(.)으로 분리하여 첫 번째 부분(호스트명) 추출
print(parsed_url.netloc.split('.')[0])  # junho85

# netloc을 점(.)으로 1회만 분리하여 두 번째 부분(도메인) 추출  
print(parsed_url.netloc.split('.', 1)[1])  # pe.kr

# path를 슬래시(/)로 분리하여 두 번째 부분(페이지 번호) 추출
print(parsed_url.path.split('/')[1])  # 1234
