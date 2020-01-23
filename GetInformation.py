from bs4 import BeautifulSoup
import re
import requests
url = "https://3g.dxy.cn/newh5/view/pneumonia"
req = requests.get(url)
req.encoding = 'utf-8'

info_raw = BeautifulSoup(req.text, 'html.parser')
titles = info_raw.find(id = "getListByCountryTypeService1")
pattern = "1[35678]\d{9}"
with open('D:\MyGit\Real-time-dynamic-query-of-pneumonia\Data Record\\text.txt','w+',encoding = 'utf-8') as file:
  file.write(titles.get_text())
  file.write('\n')
