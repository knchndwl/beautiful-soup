import requests
from bs4 import BeautifulSoup

url= BeautifulSoup('https://coinmarketcap.com/', 'html.parser')
request= requests.get(url)
data= request.text
lxml_data= BeautifulSoup(data, 'lxml')

raw_data= lxml_data.tbody
tags= raw_data.find_all('tr')
final_data= []
for m in tags:
    final_data.append(m.text.split(','))

print(final_data)

import csv
f= open('coin.csv', 'w')
x= csv.writer(f)
for m in final_data:
    x.writerow(m)

import pandas as pd

df= pd.read_csv('coin.csv')
print(df)