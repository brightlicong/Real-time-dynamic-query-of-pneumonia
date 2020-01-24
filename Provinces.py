#coding=utf-8

import re

class Province():
    def __init__(self,id,createTime,modifyTime,provinceName,provinceShortName,sort,tags):
        self.id = id
        self.creatTime = createTime
        self.modifyTime = modifyTime
        self.provinceName = provinceName
        self.provinceShortName = provinceShortName
        self.sort = sort
        
        pattern1 = re.compile(r'(?<=确诊 )\d+\.?\d*')
        pattern2 = re.compile(r'(?<=疑似 )\d+\.?\d*')
        pattern3 = re.compile(r'(?<=治愈 )\d+\.?\d*')
        pattern4 = re.compile(r'(?<=死亡 )\d+\.?\d*')
       
        try:
            self.num_confirmed = int(pattern1.findall(tags)[0])
        except:
            self.num_confirmed = 0

        try:
            self.num_suspected = int(pattern2.findall(tags)[0])
        except:
            self.num_suspected = 0

        try:
            self.num_cured = int(pattern3.findall(tags)[0])
        except:
            self.num_cured = 0

        try:
            self.num_dead = int(pattern4.findall(tags)[0])
        except:
            self.num_dead = 0
'''
此标签更新速率过慢
        self.confirmedCount = confirmedCount
        self.curedCount = curedCount
        self.deadCount = deadCount
        self.suspectedCount = suspectedCount
'''
'''
2020年01月23日
dict_keys(['id', 'createTime', 'modifyTime', 'tags', 'countryType', 'provinceId', 'provinceName', 'provinceShortName', 'sort', 'operator'])

2020年01月24日
dict_keys(['id', 'createTime', 'modifyTime', 'tags', 'countryType', 'provinceId', 'provinceName', 'provinceShortName', 'cityName', 'confirmedCount', 'suspectedCount', 'curedCount', 'deadCount', 'comment', 'sort', 'operator'])
'''