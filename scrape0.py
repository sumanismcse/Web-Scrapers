# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:33:18 2019

@author: user
"""
import requests

url= 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response= requests.get(url)
html= response.content
print (html)




