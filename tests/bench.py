# -*- coding: utf-8 -*-

import time
import requests

url_fmt = 'http://127.0.0.1:%s/diamond_classifier'

urls = [url_fmt % (8000 + i) for i in range(10)]

s = requests.Session()
payload = {'text': u'呵呵'}

count = 1
last = time.time()
while 1:
    s.post(urls[count % 10], data=payload)
    count += 1
    if count % 1000 == 0:
        now = time.time()
        print now - last
        last = now
