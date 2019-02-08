from bs4 import BeautifulSoup
import requests

r = requests.post('http://httpbin.org/post', data = {'UserId':'12345', 'Status':'On'})
print(r.status_code, r.reason)

soup = 0
response = requests.get('http://skillsmart.ru/auto/me_post.php')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")

span_list = soup.find_all('div', {'class': 'T1'})

s1 = str(span_list).split('p')
for item in s1:
    if 'cs' in item:
        item = str(item).replace('>', '').replace('<', '')
        item = item.split(' ')
        item2 = ' '
        for i in range(4):
            item2 += str(item[i]) + ' '
        item = str(item[4]) + item2
        print(item)
