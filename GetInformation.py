#coding=utf-8

from bs4 import BeautifulSoup
import re
import requests
import json
from Provinces import Province
from datetime import datetime
from functions import *

now_txt = '{}年{}月{}日-{}时{}分.txt'.format(datetime.today().year,datetime.today().month,datetime.today().day,datetime.today().hour,datetime.today().minute)
now_csv = '{}年{}月{}日-{}时{}分.csv'.format(datetime.today().year,datetime.today().month,datetime.today().day,datetime.today().hour,datetime.today().minute)

url = "https://3g.dxy.cn/newh5/view/pneumonia"
req = requests.get(url)
req.encoding = 'utf-8'

info_raw = BeautifulSoup(req.text, 'html.parser')
info_raw = info_raw.find(id = "getListByCountryTypeService1").get_text()
pattern = re.compile(r'\[.*\]')
result = pattern.search(info_raw)

result_dict = json.loads(result.group())

Province_list = []
for item in result_dict:
    Province_list.append(Province(item['id'],item['createTime'],item['modifyTime'],item['provinceName'],item['provinceShortName'],item['sort'],item['tags']))

#保存json文件
with open('D:\MyGit\Real-time-dynamic-query-of-pneumonia\Data Record\\'+now_txt,'w+',encoding = 'utf-8') as file:
    file.write(result.group())

#保存csv文件
DicToCSV(result_dict,now_csv)
ToCSV_separately(Province_list)
