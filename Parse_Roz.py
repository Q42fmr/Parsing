
import requests
from bs4 import BeautifulSoup as BS
import csv

#r = requests.get("https://collar.com/en/")
#html = BS(r.content, 'html.parser')

#for el in html.select (".title > .product_box row"):
#  title = el.select('.price > 0')
#  print(title[0].text)

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 'accept': '*/*'}
HOST = 'https://rozetka.com.ua/'
FILE = 'rozetka.csv'

def get_html (url, params = None):
  r = requests.get (url, headers=HEADERS, params=params)
  return r

def get_pages_count (html):
  soup = BS(html, 'lxml')
  pagination = soup.find_all ('a', class_='pagination__link')
  if pagination:
    return int(pagination[-1].get_text())
  else:
    return 1


def get_content (html):
  soup = BS(html, 'lxml') # создаем обьект, конструктора, с параметрами ссылки, которую парсим и типов обьекта для парсинга. Из этого обьекта создаются другие обьекты к которым мы можем обращатся и, которыми мы можем пользоватся. 
#  items = soup.find_all('div', class_='old') # Парсим цены
  items = soup.find_all('li', class_='catalog-grid__cell') # Парсим весь блок.
  spisok = []
  for item in items:
    rev = item.find('span', class_='goods-tile__reviews-link')
    old_price = item.find('div', class_='goods-tile__price--old')
    if rev: 
      rev = rev.get_text().replace(' отзывов', '')
    else:
      rev = '0 отзывов'
    if old_price:
      old_price = old_price.get_text().replace('xa0₴','')
    else:
      old_price = 'Это цена без скидки'
    spisok.append({
      'description':item.find('span', class_='goods-tile__title').get_text(strip=True),
      'price':item.find('span', class_='goods-tile__price-value').get_text(strip=True),
      'link': item.find('a', class_='goods-tile__picture').get('href'),
      'review': rev,
      'old_price' : old_price

    })
  return spisok

def save_file (items, path):
  with open(path , 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter = ';') # делимитер - разделитель
    writer.writerow(['Описание', 'Цена', 'Ссылка', 'отзывы', 'старая цена'])
    for item in items:
      writer.writerow([item['description'], item ['price'], item['link']
      , item['review']
      , item['old_price']
      ])


def parse ():
  URL = input('Введите url')
  URL = URL.strip()
  html = get_html(URL)
  if html.status_code == 200:
    spisok = []
    pages_count = get_pages_count(html.text)
    for el in range(1,pages_count + 1):
      print (f'Парсинг страницы: {el} из {pages_count}...' )
      html = get_html(URL, params = {'page':el})
      spisok.extend(get_content(html.text))
    save_file(spisok, FILE)
    print(f'получено {len(spisok)} товаров.')
  else:
    print('Error')
  

