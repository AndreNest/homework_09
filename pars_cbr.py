import requests
from bs4 import BeautifulSoup as bs
url = "https://cbr.ru"
response = requests.get(url).text
soup = bs(response, 'html.parser')
rubl_dollar = soup.find('div', class_='col-md-2 col-xs-9 _right mono-num')
rubl_inf = soup.find('div', class_="main-indicator_value")
print(f'1 $ = {rubl_dollar.text}')
print(f'Целевая инфляция = {rubl_inf.text}')