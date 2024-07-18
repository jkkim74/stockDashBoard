import requests
from bs4 import BeautifulSoup


def get_kospi_fear_and_greed_index():
    url = "https://kospi-fear-greed-index.co.kr/"

    # 네이버 금융의 KOSPI Fear and Greed Index 페이지에 GET 요청
    response = requests.get(url)

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    # KOSPI Fear and Greed Index가 포함된 태그를 찾기
    divs = soup.find_all("div","wp-block-group has-global-padding is-layout-constrained wp-block-group-is-layout-constrained")
    for idx, val in enumerate(divs):
        if idx == 1:
            print(val)
    # print(index_tag)
    # 태그에서 텍스트 추출
    # if index_tag:
    #     fear_and_greed_index = index_tag.get_text(strip=True)
    #     print(f"KOSPI Fear and Greed Index: {fear_and_greed_index}")
    # else:
    #     print("KOSPI Fear and Greed Index를 찾을 수 없습니다.")


# 함수 호출
get_kospi_fear_and_greed_index()
