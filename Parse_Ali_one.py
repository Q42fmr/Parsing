from bs4 import BeautifulSoup as BS
import requests
import Pars_Ali.Parse_Ali

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 'accept': '*/*'}
HOST = 'https://www.alibaba.com/'
URL = 'https://www.alibaba.com/premium/boost_material/'

def get_sub_content (html):
  soup = BS(html, 'html.parser')# считываем всю html страницу и создаем обьект с которым будем работать
  item = soup.find_all('h1', class_='module-pdp-title')
  print (f'АЗАЗАЗ {item} ЛОЛ')
  test = item.get_text()
  chars = set('ETPU')
  if any((c in chars) for c in test):
    print('Found')
  else:
    print('Not Found')
    item = item.get_text()
  return item

def get_total_quantity (html):
  soup = BS(html, 'html.parser')
  items = soup.find_all('span', class_='overview-item-content')
  if items:
    item = items.get_text()
  else:
    item = 'None'
  return item

def get_html (url, params = None):
  r = requests.get (url, headers=HEADERS, params=params)
  return r
