import requests as rq
from bs4 import BeautifulSoup as bs

# website link
my_url = 'https://bigshopbd.com/product-category/home-and-living'

# get website link
p_html = rq.get(my_url)

# get html text
p_soup = bs(p_html.text,'html.parser')

# find products name and price
name_con = p_soup.findAll('div',{'class':'product-content'})
price_con = p_soup.findAll('h6',{'class':'product-price'})

# select .csv file
filename = 'smartphone.csv'

# create .csv file
f = open(filename, 'w', encoding='utf-8')

# create headers of .csv file
headers = 'Phone Name, Price\n'

#add header in .csv file
f.write(headers)

# blank list for product name and price
p_name = []
p_price = []

# collect all products name and add to the p_name list
for i in name_con:
    p_name.append(i.h6.a.text)

# collect all products name and add to the p_ list
for i in price_con:
    p_price.append(i.span.b.text)

# Add all listed content to the CSV file
for i, j in zip(p_name, p_price):
    f.write(f"{i}, {j}\n")

f.close()