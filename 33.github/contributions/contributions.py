import json
import os
from dotenv import load_dotenv
import requests
import datetime
from zoneinfo import ZoneInfo  # Python 3.9 이상에서 사용 가능

# .env 파일에 있는 환경 변수 로드
load_dotenv()

# .env 파일에서 GITHUB_TOKEN 불러오기
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise Exception("GITHUB_TOKEN이 .env 파일에 설정되지 않았습니다.")

# 조회할 GitHub 사용자 이름 목록
usernames = [
    'junho85',  # 김준호
]  # 조회하고자 하는 GitHub 사용자 이름들로 변경하세요.

# 한국 표준시(KST, UTC+9) 타임존 설정
kst = ZoneInfo("Asia/Seoul")

# 오늘 날짜를 KST 기준으로 얻기
# today = datetime.datetime.now(kst).date()
start_date = datetime.date(2025, 3, 10)
# end_date = start_date + datetime.timedelta(days=99)
end_date = datetime.date(2025, 3, 12)

# KST 시간대를 가진 datetime 객체 생성
start_datetime = datetime.datetime.combine(start_date, datetime.time(0, 0, 0), tzinfo=kst)
end_datetime = datetime.datetime.combine(end_date, datetime.time(23, 59, 59), tzinfo=kst)

# GraphQL 쿼리 정의
query = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

# 요청 헤더 설정 (Bearer 토큰 인증)
headers = {
    "Authorization": f"bearer {GITHUB_TOKEN}"
}

# GitHub GraphQL API 엔드포인트
url = "https://api.github.com/graphql"

# 각 사용자에 대해 쿼리를 실행
for username in usernames:
    # 쿼리 변수 설정 (ISO 8601 포맷, 예: "2025-02-04T00:00:00+09:00")
    variables = {
        "login": username,
        "from": start_datetime.isoformat(),
        "to": end_datetime.isoformat()
    }

    # POST 요청 실행
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

    # API 응답 JSON 파싱 후 출력
    data = response.json()

    print(f"=== {username}의 기여 내역 ===")
    print(json.dumps(data, indent=2))
