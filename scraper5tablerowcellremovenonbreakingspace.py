# -*- coding: utf-8 -*-
"""
Created on Tue May 28 00:06:00 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print (cell.text.replace('&nbsp;', ''))