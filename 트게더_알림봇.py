import requests
from bs4 import BeautifulSoup
import os
import time
import telegram

bot = telegram.Bot(token = '토큰')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    req = requests.get('마루코님 트게더 링크')
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('셀렉터')
    tgd_url = posts[1].get('href')
    # 아마 텔레그램에 링크를 걸어주기 위해서 사용하실 겁니다
    # 이걸 이용해서 코드를 더 간소화하고
    # 이전에 있던 글에 대한 알림을 다시 보내는 오류를 해결할 수 있습니다
    # 이 코드를 이용하면 문자열 ex) /21457802가 반환됩니다

    with open(os.path.join(BASE_DIR, 'tgd_url.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before[1:9] < tgd_url[1:9]:
            # 여기서는 이전에 url을 저장해둔 txt 파일에서 숫자 부분만 비교합니다
            # 그 결과로 트게더에 나중에 작성된 글의 번호가 더 크다는 것을 통해
            # 이전에 작성한 글에 대한 알림을 다시 보내는 오류를 해결할 수 있습니다
            bot.sendMessage(chat_id = '채널 아이디', text='새 글이 올라왔습니다! \n' + '마루코님 트게더 링크' + tgd_url)
        f_read.close()

    with open(os.path.join(BASE_DIR, 'tgd_url.txt'), 'w+') as f_write:
        f_write.write(tgd_url)
        f_write.close()

    time.sleep(300)
    # 아직 서버에 호스팅하고 있지 않기 때문에 while문을 이용해서 5분마다 갱신하고 있습니다
    # 이러한 알고리즘을 이용할 시 주석을 제외한 30줄로 최대한의 효율을 낼 것이라고 생각합니다
