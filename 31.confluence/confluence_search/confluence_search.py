import requests
import json
import os
from getpass import getpass # 비밀번호/토큰 입력 시 터미널에 보이지 않도록 함
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# --- 설정 ---
# .env 파일에서 CONFLUENCE_BASE_URL 불러오기, 없으면 기본값 사용
CONFLUENCE_BASE_URL = os.getenv('CONFLUENCE_BASE_URL', "http://www.foobar.com/confluence")  # Confluence 인스턴스 주소
SEARCH_API_ENDPOINT = "/rest/api/content/search" # 검색 API 엔드포인트 (REST API v1 기준)
SEARCH_QUERY = "검색할 키워드" # 여기에 실제 검색하고 싶은 키워드를 입력하세요

# --- 인증 정보 ---
# 방법 1: 환경 변수 사용 (권장) - 미리 환경 변수 설정 필요
# 예: export CONFLUENCE_TOKEN='your_bearer_token'
confluence_token = os.getenv("CONFLUENCE_TOKEN")

# 방법 2: 직접 입력 (스크립트 실행 시마다 입력)
if not confluence_token:
    print("Confluence 접속 정보를 입력하세요.")
    # getpass는 터미널에서 입력 시 문자가 보이지 않게 합니다.
    confluence_token = getpass("Bearer Token: ")

# 입력값 확인
if not confluence_token:
    print("오류: Bearer 토큰을 입력해야 합니다.")
    exit()

# --- API 요청 준비 ---
search_url = f"{CONFLUENCE_BASE_URL}{SEARCH_API_ENDPOINT}"

# 요청 헤더 (Bearer 토큰 인증 포함)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {confluence_token}"
}

# 검색 파라미터 (CQL 사용)
# Confluence Query Language (CQL)을 사용하여 검색 조건을 지정합니다.
# 예: 'text ~ "{쿼리}"' : 본문, 제목 등 텍스트 필드에서 검색
# 예: 'space = "SPC" and title ~ "제목"' : 특정 스페이스에서 제목 검색
params = {
    "cql": f'text ~ "{SEARCH_QUERY}"',
    "limit": 10,  # 결과 개수 제한 (테스트용)
    # "expand": "space,body.view" # 필요한 경우 추가 정보 요청 (예: 스페이스 정보, 본문 내용)
}

# --- API 요청 실행 및 결과 처리 ---
print(f"\n'{SEARCH_QUERY}'에 대한 검색을 시작합니다...")

try:
    response = requests.get(
        search_url,
        headers=headers,
        params=params,
        timeout=30  # 30초 타임아웃 설정
    )

    # 요청 성공 여부 확인 (4xx, 5xx 상태 코드일 경우 예외 발생)
    response.raise_for_status()

    # 응답 JSON 파싱
    results = response.json()

    # 결과 출력
    print("--- 검색 결과 ---")
    print(f"총 검색 결과 수 (제한 반영 전): {results.get('totalSize', 'N/A')}")
    print(f"표시된 결과 수: {len(results.get('results', []))}")
    print("-" * 20)

    if 'results' in results and results['results']:
        for item in results['results']:
            title = item.get('title', '제목 없음')
            content_type = item.get('type', '알 수 없음') # page, blogpost, comment, attachment 등
            link_path = item.get('_links', {}).get('webui', '')
            full_link = f"{CONFLUENCE_BASE_URL}{link_path}" if link_path else "링크 없음"
            last_modified = item.get('version', {}).get('when', '날짜 정보 없음') # 마지막 수정일

            print(f"타입: {content_type}")
            print(f"제목: {title}")
            print(f"링크: {full_link}")
            print(f"최종 수정일: {last_modified}")
            print("-" * 10)
    else:
        print("검색 결과가 없습니다.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP 오류 발생: {http_err}")
    print(f"응답 코드: {response.status_code}")
    # 오류 응답 내용 출력 시도
    try:
        error_details = response.json()
        print("오류 상세:")
        print(json.dumps(error_details, indent=2, ensure_ascii=False)) # 한글 깨짐 방지
    except json.JSONDecodeError:
        print(f"오류 응답 내용 (JSON 아님): {response.text}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"연결 오류 발생: {conn_err}")
    print(f"{CONFLUENCE_BASE_URL} 주소에 접근할 수 있는지 확인하세요.")
except requests.exceptions.Timeout as timeout_err:
    print(f"요청 시간 초과: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"요청 중 알 수 없는 오류 발생: {req_err}")
except json.JSONDecodeError:
    print("오류: API 응답이 유효한 JSON 형식이 아닙니다.")
    print(f"응답 코드: {response.status_code}")
    print(f"응답 내용: {response.text}")
