import requests as rq

from bs4 import BeautifulSoup as bs

my_url = 'https://bigshopbd.com/product-category/home-and-living'

p_html = rq.get(my_url)

p_soup = bs(p_html.text,'html.parser')

name_con = p_soup.findAll('div',{'class':'product-content'})
price_con = p_soup.findAll('h6',{'class':'product-price'})


filename = 'smartphone.csv'

f = open(filename, 'w')

headers = 'Phone Name, Price\n'

f.write(headers)

p_name = []
p_price = []

for i in name_con:
    p_name.append(i.h6.a.text)

for i in price_con:
    p_price.append(i.span.b.text)

print(p_price)
