import requests
from bs4 import BeautifulSoup as BS
import csv
import Pars_Ali.Parse_Ali_one

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 'accept': '*/*'}
HOST = 'https://www.alibaba.com/'
URL = 'https://www.alibaba.com/premium/boost_material/--------------------------------L/'

def get_html (url, params = None):
  r = requests.get (url, headers=HEADERS, params=params)
  return r

def get_pages_count (html):
  soup = BS(html, 'html.parser')
  pagination = soup.find_all ('a', class_='seb-pagination__pages-link')
  if pagination:
    return int(pagination[-1].get_text())
  else:
    return 1

def get_content (html):
  soup = BS(html, 'html.parser') # создаем обьект, конструктора, с параметрами ссылки, которую парсим и типов обьекта для парсинга. Из этого обьекта создаются другие обьекты к которым мы можем обращатся и, которыми мы можем пользоватся. 
#  items = soup.find_all('div', class_='old') # Парсим цены
  items = soup.find_all('div', class_='list-no-v2-outter J-offer-wrapper') # Парсим весь блок.
  spisok = []
  for item in items:
    links = 'https:' + item.find('a', class_='elements-title-normal').get('href')
    link = links.strip()
    link =  get_html(link)
    if link.status_code == 200:
      buyer = Pars_Ali.Parse_Ali_one.get_sub_content(link.text)
      if buyer == 'delete':
        pass
      else:
        rev = item.find('span', 'seb-supplier-review__review-count_list')
        mid_rev = item.find('span', 'seb-supplier-review__score')
        if rev:
          rev = rev.get_text()
          mid_rev = mid_rev.find_next('span').get_text()
        else:
          rev = 0
          mid_rev = 0
        spisok.append({
          'description':item.find('p', class_='elements-title-normal__content').get_text(strip = True),
          'price':item.find('span', class_='elements-offer-price-normal__price').get_text(strip=True),
          'link': links,
          'review': rev,
          'midle_review' : mid_rev,
          'total buyer' : buyer
    })
  return spisok

def save_file (items, path):
  with open(path , 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter = ';') # делимитер - разделитель
    writer.writerow(['Описание', 'Цена', 'Ссылка', 'отзывы', 'старая цена'])
    for item in items:
      writer.writerow([
        item['description'], item ['price'], item['link'], item['review'], item['old_price']
      ])


def parse():
  spisok = []
  string = int(input('Сколько страниц?: '))
  for el in range(1,string):
    url = URL + str(el) + '.html'
    url = url.strip()
    html = get_html(url)
    if html.status_code == 200:
      spisok.extend(get_content(html.text))
    else:
        print ('LOLina')
  print (spisok)


  

  #pages_count = get_pages_count(html.text)
    #for el in range(1,pages_count + 1):
    #  print (f'Парсинг страницы: {el} из {pages_count}...' )
    #  html = get_html(URL, params = {'':el})
    #  spisok.extend(get_content(html.text))
    #save_file(spisok, FILE)
    #print(f'получено {len(spisok)} товаров.')
  

