from bs4 import BeautifulSoup
import requests

soup = 0
response = requests.get('https://yandex.ru/images/search?text=дерево')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
else:
    print('ERROR', response.status_code)

span_list = soup.find_all('img', {'class': 'serp-item__thumb justifier__thumb'})

print(span_list, soup)