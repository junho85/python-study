import requests
import json
import os
import sys
from getpass import getpass
import html2text
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# --- 설정 ---
# .env 파일에서 CONFLUENCE_BASE_URL 불러오기, 없으면 기본값 사용
CONFLUENCE_BASE_URL = os.getenv('CONFLUENCE_BASE_URL', "http://www.foobar.com/confluence")  # Confluence 인스턴스 주소
CONTENT_API_ENDPOINT = "/rest/api/content"  # 콘텐츠 API 엔드포인트

def get_auth_info():
    """Bearer 토큰 인증 정보를 가져오는 함수 (.env 파일 또는 사용자 입력)"""
    # .env 파일에서 인증 정보 불러오기 시도
    confluence_token = os.getenv('CONFLUENCE_TOKEN')

    # 환경 변수에 인증 정보가 있으면 그대로 사용
    if confluence_token:
        print("환경 변수에서 인증 토큰을 불러왔습니다.")
        return confluence_token

    # 환경 변수에 인증 정보가 없으면 사용자에게 입력 요청
    print("환경 변수에서 인증 토큰을 찾을 수 없습니다.")
    print("Confluence 접속 정보를 입력하세요.")
    confluence_token = getpass("Bearer Token: ")

    # 입력값 확인
    if not confluence_token:
        print("오류: Bearer 토큰을 입력해야 합니다.")
        sys.exit(1)

    return confluence_token

def get_confluence_page(page_id, token, expand="body.storage"):
    """Confluence 페이지 내용을 가져오는 함수"""
    url = f"{CONFLUENCE_BASE_URL}{CONTENT_API_ENDPOINT}/{page_id}"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    params = {
        "expand": expand  # body.storage는 HTML 형식의 콘텐츠를 가져옴
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30
        )

        # 요청 성공 여부 확인
        response.raise_for_status()

        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 오류 발생: {http_err}")
        print(f"응답 코드: {response.status_code}")
        try:
            error_details = response.json()
            print("오류 상세:")
            print(json.dumps(error_details, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print(f"오류 응답 내용 (JSON 아님): {response.text}")
        sys.exit(1)
    except (requests.exceptions.ConnectionError, 
            requests.exceptions.Timeout, 
            requests.exceptions.RequestException) as err:
        print(f"요청 중 오류 발생: {err}")
        sys.exit(1)

def convert_html_to_markdown(html_content):
    """HTML 콘텐츠를 Markdown으로 변환하는 함수"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_tables = False
    h.body_width = 0  # 줄 바꿈 없음

    return h.handle(html_content)

def save_to_markdown_file(title, content, page_id):
    """Markdown 콘텐츠를 파일로 저장하는 함수"""
    # 파일명에 사용할 수 없는 문자 제거
    safe_title = "".join([c for c in title if c.isalnum() or c in " _-"]).strip()
    safe_title = safe_title.replace(" ", "_")

    filename = f"{safe_title}_{page_id}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename

def main():
    # 명령줄 인수 확인
    if len(sys.argv) != 2:
        print("사용법: python confluence_to_markdown.py <페이지_ID>")
        sys.exit(1)

    page_id = sys.argv[1]

    # 인증 정보 가져오기
    token = get_auth_info()

    print(f"Confluence 페이지 ID {page_id}의 내용을 가져오는 중...")

    # 페이지 정보 가져오기
    page_data = get_confluence_page(page_id, token)

    # 페이지 제목과 HTML 콘텐츠 추출
    title = page_data.get("title", "Untitled")
    html_content = page_data.get("body", {}).get("storage", {}).get("value", "")

    if not html_content:
        print("오류: 페이지 내용을 가져올 수 없습니다.")
        sys.exit(1)

    print(f"페이지 '{title}'의 내용을 Markdown으로 변환하는 중...")

    # HTML을 Markdown으로 변환
    markdown_content = convert_html_to_markdown(html_content)

    # Markdown 파일로 저장
    filename = save_to_markdown_file(title, markdown_content, page_id)

    print(f"변환 완료! 파일이 저장되었습니다: {filename}")

if __name__ == "__main__":
    main()
