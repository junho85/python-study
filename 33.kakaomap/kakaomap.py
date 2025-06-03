import requests
from dotenv import load_dotenv
import os


def get_restaurant_list_in_seoul(query="맛집", x=126.9784147, y=37.5666805, radius=20000):
    """
    카카오 로컬 API를 사용하여 서울 지역의 맛집 리스트를 조회하는 함수

    :param query: 검색 키워드 (기본값: '맛집')
    :param x: 중심좌표의 경도(Longitude) (서울시청 기준 예시)
    :param y: 중심좌표의 위도(Latitude) (서울시청 기준 예시)
    :param radius: 중심좌표로부터의 검색 반경 (단위: 미터, 최대 20,000)
    :return: 맛집 리스트 (dict 형태)
    """
    # .env 파일에서 환경 변수 로드
    load_dotenv()

    # 카카오 REST API 키
    REST_API_KEY = os.getenv('KAKAO_REST_API_KEY')
    if not REST_API_KEY:
        raise ValueError("KAKAO_REST_API_KEY environment variable is not set")

    # 헤더 설정
    headers = {
        "Authorization": f"KakaoAK {REST_API_KEY}"
    }

    # 파라미터 설정
    params = {
        "query": query,  # 검색 키워드
        "category_group_code": "FD6",  # 음식점(category_group_code=FD6) 범주로 제한 (선택)
        "x": x,  # 중심 좌표 (경도)
        "y": y,  # 중심 좌표 (위도)
        "radius": radius,  # 검색 반경 (최대 20,000)
        "size": 15  # 한 페이지에 보여질 문서의 개수(기본 15, 최대 45)
    }

    url = "https://dapi.kakao.com/v2/local/search/keyword.json"

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None


if __name__ == "__main__":
    # 서울 시청을 기준으로 반경 20km 내 '맛집' 검색
    result = get_restaurant_list_in_seoul(query="판교맛집")  # 20km

    if result:
        documents = result.get("documents", [])

        print(f"검색된 맛집 수: {len(documents)}")
        for idx, place in enumerate(documents, start=1):
            place_name = place.get("place_name")
            address_name = place.get("road_address_name") or place.get("address_name")
            phone = place.get("phone")
            print(f"[{idx}] {place_name}\n     주소: {address_name}\n     전화번호: {phone}")
