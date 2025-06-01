"""
pytz 모듈을 사용하여 현재 시스템의 타임존 정보를 가져오는 예제입니다.
pytz는 파이썬에서 타임존을 처리하기 위한 라이브러리입니다.

pytz 모듈을 설치해야 합니다.
pip install pytz
"""
import datetime
import pytz

# 현재 시간을 가져옵니다.
now = datetime.datetime.now()

# 현재 시스템의 타임존을 확인합니다.
timezone = datetime.datetime.now(pytz.timezone('UTC')).astimezone().tzinfo

# 타임존 정보 출력
print(timezone)


