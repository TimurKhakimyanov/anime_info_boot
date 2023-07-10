# from bs4 import BeautifulSoup
# import requests
# from fake_useragent import UserAgent

# ua = UserAgent()
# header = {
#     "User-Agent" : ua.random
# }

# query = input('What are you searching for?:   ' )
# url ='https://shikimori.me/animes?search='
# page = requests.get(url + query, headers=header)
# soup = BeautifulSoup(page.text, 'lxml')
# print(page.status_code)
# print(page.text)
# # print(page.text)
# # h3 = soup.find_all("h3",class_="r")
# # for elem in h3:
# # 	elem=elem.contents[0]
# # 	link=("https://www.google.com" + elem["href"])
# # 	print(link)

import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = {
    "User-Agent" : ua.random
}

url = "https://shikimori.me/animes?search=%D0%BF%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD(2023)"  # Замените на фактический URL-адрес

response = requests.get(url, allow_redirects=False, headers=header)

# Обрабатываем ответ
if response.status_code == 200:
    print("Запрос успешно выполнен")
elif response.status_code == 301 or response.status_code == 302:
    print("Получен ответ с кодом перенаправления")
    redirect_url = response.url
    print("Запрос был перенаправлен на:", redirect_url)
    # Обрабатываем переадресацию
else:
    print(f"Ошибка выполнения запроса: {response.status_code}")