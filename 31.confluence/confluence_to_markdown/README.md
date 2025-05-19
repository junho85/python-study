# Confluence to Markdown Converter

이 스크립트는 Confluence 위키의 문서 ID를 기반으로 해당 페이지의 내용을 Markdown 형식으로 저장합니다.

## 기능

- Confluence 페이지 ID를 입력받아 해당 페이지의 내용을 가져옵니다.
- HTML 형식의 Confluence 콘텐츠를 Markdown으로 변환합니다.
- 변환된 Markdown 콘텐츠를 파일로 저장합니다.

## 설치 방법

1. 필요한 패키지 설치:

```bash
pip install -r requirements.txt
```

## 환경 변수 설정 (선택 사항)

스크립트는 .env 파일에서 환경 변수를 로드하여 Confluence 접속 정보를 설정할 수 있습니다:

1. 프로젝트 디렉토리에 `.env` 파일을 생성합니다 (`.env_sample` 파일을 참고하세요):

```
CONFLUENCE_BASE_URL=https://your-confluence-instance.com
CONFLUENCE_TOKEN=your_bearer_token
```

2. 각 변수에 적절한 값을 입력합니다:
   - `CONFLUENCE_BASE_URL`: Confluence 인스턴스의 기본 URL
   - `CONFLUENCE_TOKEN`: Confluence API에 접근하기 위한 Bearer 토큰

## 사용 방법

1. 명령줄에서 다음과 같이 실행합니다:

```bash
python confluence_to_markdown.py <페이지_ID>
```

2. 환경 변수가 설정되어 있지 않은 경우, 프롬프트에 따라 Confluence Bearer 토큰을 입력합니다.

3. 스크립트가 페이지 내용을 가져와 Markdown으로 변환한 후, 현재 디렉토리에 파일로 저장합니다.

## 예시

```bash
python confluence_to_markdown.py 123456
```

위 명령은 ID가 123456인 Confluence 페이지를 가져와 Markdown으로 변환하고 저장합니다.

## 참고 사항

- 이 스크립트는 Confluence REST API를 사용하여 페이지 내용을 가져옵니다.
- 인증 방식으로 Bearer 토큰 방식을 사용합니다.
- HTML을 Markdown으로 변환하기 위해 `html2text` 라이브러리를 사용합니다.
- 환경 변수 로딩을 위해 `python-dotenv` 라이브러리를 사용합니다.
- 저장된 파일 이름은 페이지 제목과 ID를 기반으로 생성됩니다.
- `.env` 파일은 버전 관리 시스템에 포함되지 않도록 `.gitignore`에 추가하는 것이 좋습니다.
