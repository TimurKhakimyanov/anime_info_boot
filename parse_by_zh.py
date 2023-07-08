from bs4 import BeautifulSoup as bs
from googlesearch import search
import requests 
import undetected_chromedriver as uc
from fake_useragent import UserAgent



ua = UserAgent()
header = {
    "User-Agent" : ua.random
}

def google_search():
    search_res = ''
    query = input("Enter your search query: ") + "shikimori"

    for result in search(query, num_results=1):
        search_res = result
        break

    return search_res

def parse_bs(url):
    get_html = requests.get(url, headers= header)
    soup = bs(get_html.content, 'html.parse')
    return soup


def parse_page():
    search_res = google_search()
    driver = uc.Chrome(headless=True,use_subprocess=False)
    url = driver.get(search_res)
    res = parse_bs(url)
    return res



a = parse_page()
print(a)