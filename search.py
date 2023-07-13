# # from bs4 import BeautifulSoup
# # import requests
# # from fake_useragent import UserAgent

# # ua = UserAgent()
# # header = {
# #     "User-Agent" : ua.random
# # }

# # query = input('What are you searching for?:   ' )
# # url ='https://shikimori.me/animes?search='
# # page = requests.get(url + query, headers=header)
# # soup = BeautifulSoup(page.text, 'lxml')
# # print(page.status_code)
# # print(page.text)
# # # print(page.text)
# # # h3 = soup.find_all("h3",class_="r")
# # # for elem in h3:
# # # 	elem=elem.contents[0]
# # # 	link=("https://www.google.com" + elem["href"])
# # # 	print(link)

# import requests
# from fake_useragent import UserAgent

# ua = UserAgent()
# header = {
#     "User-Agent" : ua.random
# }

# url = "https://shikimori.me/animes?search=%D0%BF%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD(2023)"  # Замените на фактический URL-адрес

# response = requests.get(url, allow_redirects=False, headers=header)

# # Обрабатываем ответ
# if response.status_code == 200:
#     print("Запрос успешно выполнен")
# elif response.status_code == 301 or response.status_code == 302:
#     print("Получен ответ с кодом перенаправления")
#     redirect_url = response.url
#     print("Запрос был перенаправлен на:", redirect_url)
#     # Обрабатываем переадресацию
# else:
#     print(f"Ошибка выполнения запроса: {response.status_code}")

import requests

# Выполнение GET-запроса
response = requests.get("https://shikimori.me/animes?search=%D0%91%D0%B5%D0%BD%D0%B7%D0%BE%D0%BF%D0%B8%D0%BB%D0%B0")

# Получение URL, на который был перенаправлен запрос
redirect_url = response.url

# Вывод перенаправленного URL
print("Перенаправленный URL:", redirect_url)
