'''
심슨 시즌 1-9 대본 크롤링해오기.
'''
import requests
from bs4 import BeautifulSoup

for i in range(1000):

    # 사이트 주소 형식
    website = f"https://transcripts.foreverdreaming.org/viewtopic.php?f=431&t={i+21861}"

    # 사이트 내용 받이오기
    page = requests.get(website)
    soup = BeautifulSoup(page.content, 'html.parser')

    # 요소 찾기
    content = soup.find(id='pagecontent')
    title = content.find("div", {"class": "boxheading"})
    body = content.find("div", {"class": "postbody"})

    # 텍스트 가공
    title = title.text
    title = title.rstrip()
    title = title.lstrip()

    script = body.text
    script = script.rstrip()
    script = script.lstrip()
    script = script.replace('\n\n', '')

    # 시즌, 에피소드 번호 얻기
    season, episode = int(title[0:2]), int(title[3:5])

    # 루프 종료 조건
    if season >= 10:
        break

    # 최종적으로 쓸 내용
    data = title + '\n' + '-'*50 + '\n' + script

    # 파일 저장
    with open(f"data/Season_{season}/episode_{episode}", "w", encoding='utf-8') as file:
        file.write(data)