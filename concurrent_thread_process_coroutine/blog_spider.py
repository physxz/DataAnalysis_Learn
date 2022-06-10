from bs4 import BeautifulSoup
import requests

urls = [
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1, 50+1)
]

def craw(url): # craw就是生产者，生产结果为html
    r = requests.get(url)
    return r.text

def parse(html): # parse是html里解析出来的链接和标题
    # class="post-item-title"
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='post-item-title') # class_就是html的'a'标签里的class属性，易跟class类混淆，所以加下划线
    return [(link['href'], link.get_text()) for link in links]

if __name__ == '__main__':
    for result in parse(craw((urls[2]))):
        print(result)