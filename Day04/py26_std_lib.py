#표준 라이브러리
#import datetime as dt
from datetime import date, datetime

first_date = date(2022, 12, 25)
print(first_date)

cur_date = date.today()
print(cur_date)

print(cur_date - first_date)

cur_dt = datetime.now()
print(cur_dt)
print(cur_dt.strftime('%Y-%m-%d')) #date.today() str

print(cur_dt.weekday()) # 0부터 월요일
print(cur_dt.isoweekday()) # 1부터 월요일

import time

for x in range(10):
    print(x)
    time.sleep(0.001) # second C#, java, C++ time.sleep(ms)

import math

print(math.pi)

import os
# print(os.environ)
# print(os.environ['PATH'])

print(os.getcwd())

print(os.system('dir'))
print(os.system('git --version'))

import json
with open('./Day04/data.json','r',encoding='utf-8') as f:
    data = json.load(f)

print(data)

##urllib

from urllib.request import urlopen

res = urlopen('https://www.naver.com')
print(res.status) # 200 OK
print(res.read().decode('utf-8')) # index.html 가져옴 --> 웹 크롤링 


import webbrowser

print(webbrowser.get())

url = 'http://www.naver.com'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
#프로그램을 종료하면 웹브라우저도 같이 닫힘
