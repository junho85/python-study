import datetime
from zoneinfo import ZoneInfo

# 방법 1: 시스템 로컬 타임존 사용
now_local = datetime.datetime.now(datetime.timezone.utc).astimezone()
print("방법 1 - 시스템 로컬 타임존:")
print(f"현재 시간: {now_local}")
print(f"타임존 오프셋: {now_local.utcoffset()}")
print(f"타임존 정보: {now_local.tzinfo}")
print()

# 방법 2: UTC 타임존 사용
now_utc = datetime.datetime.now(datetime.timezone.utc)
print("방법 2 - UTC 타임존:")
print(f"UTC 시간: {now_utc}")
print(f"타임존 오프셋: {now_utc.utcoffset()}")
print(f"타임존 정보: {now_utc.tzinfo}")
print()

# 방법 3: 특정 타임존 지정 (Python 3.9+에서 zoneinfo 사용)
seoul_tz = ZoneInfo("Asia/Seoul")
now_seoul = datetime.datetime.now(seoul_tz)
print("방법 3 - 서울 타임존:")
print(f"서울 시간: {now_seoul}")
print(f"타임존 오프셋: {now_seoul.utcoffset()}")
print(f"타임존 정보: {now_seoul.tzinfo}")
print()

# 방법 4: 수동 오프셋 지정
kst = datetime.timezone(datetime.timedelta(hours=9))
now_kst = datetime.datetime.now(kst)
print("방법 4 - 수동 KST 오프셋:")
print(f"KST 시간: {now_kst}")
print(f"타임존 오프셋: {now_kst.utcoffset()}")
print(f"타임존 정보: {now_kst.tzinfo}")
print()

# 방법 5: 기존 naive datetime을 aware datetime으로 변환
naive_now = datetime.datetime.now()
aware_now = naive_now.replace(tzinfo=datetime.timezone.utc)
print("방법 5 - Naive를 Aware로 변환:")
print(f"변환된 시간: {aware_now}")
print(f"타임존 오프셋: {aware_now.utcoffset()}")
print(f"타임존 정보: {aware_now.tzinfo}")
