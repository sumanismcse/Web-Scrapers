# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:50:15 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup
url= 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response= requests.get(url)
html= response.content

soup=BeautifulSoup(html)
table=soup.find('tbody',attrs={'class':'stripe'})
print (table.prettify())