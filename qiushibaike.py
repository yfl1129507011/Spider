import requests
from bs4 import BeautifulSoup

def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text

def get_content(url, page):
    html = download_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    content_id = soup.find(id='content')
    if content_id is not None:
        content_list = content_id.find_all('div', class_='article')  # 找到文章列表
        output = """来自第{}页 【作者】{} 【性别】{} 【年龄】{} 【好笑数】{} 【评论数】{}\n{}\n~~~~~~~~~~~~~~~~~~~~~~\n"""  # 定义内容输出格式
        for i in content_list:
            author = i.find('h2').string   # 获取作者名称
            content = i.find('div', class_='content').find('span').get_text()   # 获取内容
            stats = i.find('div', class_='stats')
            votes = stats.find('span', class_='stats-vote').find('i', class_='number').string   # 获取好笑数
            comments = stats.find('span', class_='stats-comments').find('i', class_='number').string  # 获取评论数
            author_info = i.find('div', class_='articleGender')
            gender = ''   # 性别
            age = ''      # 年龄
            if author_info is not None:
                class_list = author_info['class']    # ['articleGender', 'womenIcon']
                if 'womenIcon' in class_list:
                    gender = '女'
                elif 'manIcon' in class_list:
                    gender = '男'

                age = author_info.string

            print(output.format(page, author, gender, age, votes, comments, content))
            # save_txt(output.format(page, author, gender, age, votes, comments, content))

def save_txt(*args):
    for i in args:
        with open('qiubai.txt', 'a', encoding='utf-8') as f:
            f.write(i)

def main():
    for i in range(1, 14):
        url = "https://www.qiushibaike.com/text/page/{}".format(i)
        get_content(url, i)

if __name__ == '__main__':
    main()