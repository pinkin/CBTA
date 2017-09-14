# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:02:01 2017

@author: jrbrad
"""

import requests
from bs4 import BeautifulSoup as bs
    
my_wm_username = 'pnathani'
search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content
            
parsed_html = bs(response,'lxml')
target_rows=parsed_html.find_all('tr')



print
my_result_list=[]
for rows in target_rows:
    new_row = [] 
    for x in rows.find_all('td'):
        new_row.append(x.text.encode("ascii",'ignore'))
        #x.text.encode("ascii",'ignore')
    my_result_list.append(new_row)
    
print '\nHere\'s the Data'


print my_wm_username
print len(my_result_list)
print my_result_list