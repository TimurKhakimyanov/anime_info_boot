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
    a = txtt + " shikimori"
    url = next(search(a, num_results= 1))
    print(url)
    rs = requests.get(url, headers = header)
    bs1 = BeautifulSoup(rs.text, 'lxml')
    bs2 = bs1.find('div', class_ = 'c-info-left')
    for div in bs2:
        divvv.append(div.text)
    bs3 = bs2.find('span', class_ = "b-anime_status_tag released")
    bs4 = bs3.get('data-text')
    sts = bs4
    bs5 = bs1.find('div', class_ = "b-text_with_paragraphs")
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