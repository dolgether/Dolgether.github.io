import requests
from bs4 import BeautifulSoup
import os
import telegram

bot = telegram.Bot(token='aaaa:bbbbbbbb') # 여기에 봇 토큰 넣으시구요

base_dir = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://tgd.kr/im_ssoju')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('#article-list>.article-list-row>.item>.list-title>a')
writer = soup.select('#article-list>.article-list-row>.item>.list-title>.list-writer>span')
    
for i in range(0, 10):
    tgd_url = posts[i].get('href')
    writer_name = writer[i].text.strip()
    if tgd_url[10:14] != "page" and writer_name == "쏘주님":
        with open(os.path.join(base_dir, 'im_ssoju_url.txt'), 'r+') as f_read:
            before = f_read.readline()
            f_read.close()
            if before[1:9] < tgd_url[1:9]:
                bot.sendMessage(chat_id = '', text='문구 \n' + 'https://tgd.kr' + tgd_url)
                                # 문구 부분에는 쏘주님이 트게더에 글을 쓰셨어요! 등의 문구가 들어가면 됩니다
                                # chat_id는 https://api.telegram.org/botaaaa:bbbbbbbb/getUpdates 에서 확인할 수 있어요
                                # aaaa:bbbbbbbb 는 임의의 토큰이에오
                with open(os.path.join(base_dir, 'im_ssoju_url.txt'), 'w+') as f_write:
                    f_write.write(tgd_url)
                    f_write.close()
