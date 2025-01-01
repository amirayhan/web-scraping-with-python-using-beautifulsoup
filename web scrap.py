import requests as rq

from bs4 import BeautifulSoup as bs

my_url = 'https://www.othoba.com/smartphone'

p_html = rq.get(my_url)

p_soup = bs(p_html.text,'html.parser')
print(p_soup)

