import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from googlesearch import search

ua = UserAgent()
header = {
    "User-Agent" : ua.random
}

def get_url(txtt):
    divv = []
    divvv = []
    a = txtt 
    url = 'https://shikimori.me/animes?search=' + a
    print(url)
    rs = requests.get(url, headers = header, allow_redirects=False)
    if rs.status_code == 200:
        bs21 = BeautifulSoup(rs.text, 'lxml')
        bs22 = bs21.find('a', class_ = 'cover anime-tooltip')
        bs23 = bs22.get('href')
        print(bs23)
        bs24 = requests.get(bs23, headers=header)
    elif rs.status_code == 301 or rs.status_code == 302:
        bs24 = requests.get(url, headers=header)
    bs1 = BeautifulSoup(bs24.text, 'lxml')
    bs2 = bs1.find('div', class_ = 'c-info-left')
    for div in bs2:
        divvv.append(div.text)
    bs3 = bs2.find('span', class_ = "b-anime_status_tag released")
    if bs3 == None:
        bs3 = bs2.find('span', class_ = "b-anime_status_tag ongoing")
    bs4 = bs3.get('data-text')
    sts = bs4
    bs5 = bs1.find('div', class_ = "b-text_with_paragraphs")
    if bs5 == None:
        divv.append("Нет описания")
    else:
        for a in bs5:
            divv.append(a.text)
    txtt = url
    return {"url" : txtt, "desc" : divv, "tags" : divvv, "stat" : sts }
    

def get_pic(url):
    rs = requests.get(url, headers = header)
    bs1 = BeautifulSoup(rs.text, 'lxml')
    bs2 = bs1.find('div', class_ = "c-poster")
    bs3 = bs2.find('picture')
    
    bs4 = bs3.find('img').get('src')
    bs5 = requests.get(bs4, headers= header).content
    with open('123.jpg', 'wb') as file:
        file.write(bs5)

# get_url(txtt)
# get_pic()