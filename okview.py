import os
import requests
from bs4 import BeautifulSoup
import ffmpy3
from multiprocessing.dummy import Pool as ThreadPool

search_keyword = '权力的游戏'
search_url = 'http://www.jisudhw.com/index.php'
search_params = {
    'm': 'vod-search'
}  # url参数

search_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Referer': 'http://www.jisudhw.com',
    'Origin': 'http://www.jisudhw.com',
    'Host': 'www.jisudhw.com'
}
search_datas = {
    'wd': search_keyword,
    'submit': 'search'
}

video_dir = ''

r = requests.post(url=search_url, params=search_params, headers=search_headers, data=search_datas)
r.encoding = 'utf-8'
server = 'http://www.jisudhw.com'
search_html = BeautifulSoup(r.text, 'html.parser')
search_spans = search_html.find_all('span', class_='xing_vb4')
for span in search_spans:
    url = server + span.a.get('href')
    name = span.a.string
    print(url)
    print(name)
    video_dir = name
    if name not in os.listdir('./'):
        os.mkdir(name)

    detail_url = url
    r = requests.get(url=detail_url)
    r.encoding = 'utf-8'
    detail_bf = BeautifulSoup(r.text, 'html.parser')
    num = 1
    search_res = {}
    for each_url in detail_bf.find_all('input'):
        if 'm3u8' in each_url.get('value'):
            url = each_url.get('value')
            if url not in search_res.keys():
                search_res[url] = num
            print('第%03d集:' % num)
            print(url)
            num += 1

def downVideo(url):
    num = search_res[url]
    name = os.path.join(video_dir, '第%03d集.mp4' % num)
    ffmpy3.FFmpeg(inputs={url: None}, outputs={name: None}).run()

pool = ThreadPool(10)
results = pool.map(downVideo, search_res.keys())