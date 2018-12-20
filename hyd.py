# -*- coding: utf-8 -*-
# @Date    : 2018-12-20 10:54:14
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import os
import re
import time
import json
import requests
from datetime import datetime

class HYDSpider(object):
    """docstring for HYDSpider"""
    def __init__(self):
        self.url = 'http://123.127.175.45:8082/ajax/GwtWaterHandler.ashx'
        self.headers = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9',
            'Connection':'keep-alive',
            'Content-Length':'21',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Host':'123.127.175.45:8082',
            'Origin':'http://123.127.175.45:8082',
            'Referer':'http://123.127.175.45:8082/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',

        }
        self.fp = open('./hdydata.json','a',encoding='utf-8')

    def crawl(self):
        r = requests.get(url=self.url,headers=self.headers,data={'Method': 'SelectRealData'})

        print(r.text)
        res = json.loads(r.text)
        return res

    def save_data(self,item):
        data = json.dumps(item,ensure_ascii=False)
        self.fp.write(data+'\n')


    def main(self):
        items = self.crawl()
        for item in items:
            self.save_data(item)



if __name__ == '__main__':
    hyd = HYDSpider()
    hyd.main()

