# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:26:49 2016

@author: Mahfuzul Alam
"""

import requests
from bs4 import BeautifulSoup

techCrunch = requests.get('https://techcrunch.com/')
parsedHtml = BeautifulSoup(techCrunch.text, 'lxml')

rows = parsedHtml.find_all(class_='block-content')

for row in rows:
    print('Title: '+ row.find('h2').text)
    print('Link: '+ row.find('a').get('href'))
    print('Logo: '+ row.findAll('img')[0].get('src'))
    print('*************************************')

