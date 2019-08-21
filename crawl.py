
# error1. bs로 하는데 그냥 html 파싱해오면 알맹이가 없음
# -> 페이지 형태가 로딩되고, 그 이후에 요청해서 알맹이 가져오는 형태
# --> 개발자도구에서, network에서 요청 request / url을 찾아서 해야함(예전에 투빅스 크롤링때 그랬듯잉)

# error2. bs로 긁어온게, html이 아니라 json형태라서 파싱이 잘 안됨.
# --> json 형태로 읽어와서 dictionary로 작업?


# is sticky로 파란블락 판단
import json
import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.kaggle.com/forums/275877/topics.json?sortBy=new&group=all&page=1&pageSize=20&category=all&turbolinks%5BrestorationIdentifier%5D=0a58a85e-cc59-4747-9a42-065885623322',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦

soup = BeautifulSoup(data.text, 'html.parser')
#soup = BeautifulSoup(data.headers, 'html.parser')
#tmp = soup.select('body > main > div > div.site-layout__main-content > div > div > div.competition > div.smart-list.smart-list--standard.undefined > div.content-box > div.content-box__content-section > div.smart-list__content > div > div')

raw_dict = json.loads(str(soup))

#for i in range(0,len(raw_dict['topics'])):
i=0
print(raw_dict['topics'][i]['title'])
topics_url = raw_dict['topics'][i]['topicUrl']
url_tmp = topics_url.split('/')
url_tmp2 = url_tmp[len(url_tmp)-1]
topic_num =url_tmp2.split('#')[0]

#내용있는 걸로 topic url 갱신
# tp : topic
topic_url = 'http://kaggle.com/topics/' + topic_num +'.json'
print(topic_url)
data_tp = requests.get(topic_url, headers=headers)
tmp = json.loads(data_tp.text)
soup_content = BeautifulSoup(tmp['comment']['content'], 'html.parser')

print(soup_content.text)
# 이거 정리해서 db에 넣고, 1시간텀해야하고
# 요약알고리즘 찾아보기


