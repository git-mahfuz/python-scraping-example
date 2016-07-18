# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
from bs4 import BeautifulSoup

postOffice = requests.get('http://www.bangladeshpost.gov.bd/PostCodeList.asp?DivID=7')
parsedHtml = BeautifulSoup(postOffice.text, 'lxml')

rows = parsedHtml.find_all('tr')

realDataStartsAtPosition = 0
data = []


for row in rows:
    tds = row.find_all('td')
    
    if len(tds) == 4 and len(tds[3].text) == 4:

        thisData = {
                    'city'  :  tds[0].text,
                    'zone'  :  tds[1].text + ' - ' + tds[2].text,
                    'zip'   :  tds[3].text
             }

        data.append(thisData)
        
        print(tds[0].text + ' / ' + tds[1].text + ' - ' + tds[2].text + ' / ' + tds[3].text)
        

with open('rangpur.json', 'w') as f:
    json.dump(data, f)
