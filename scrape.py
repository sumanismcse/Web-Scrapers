# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:48:30 2019

@author: user
"""

import requests
from bs4 import BeautifulSoup
url= 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response= requests.get(url)
html= response.content
print (html)

soup=BeautifulSoup(html)
print (soup.prettify())
