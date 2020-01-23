#dict_keys(['id', 'createTime', 'modifyTime', 'tags', 'countryType', 'provinceId', 'provinceName', 'provinceShortName', 'sort', 'operator'])
class City():
    def __init__(self,id,createTime,modifyTime,tags,provinceName,provinceShortName,sort):
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
            self.num_diagnosed = int(pattern1.findall(tags)[0])
        except:
            self.num_diagnosed = 0

        try:
            self.num_suspected = int(pattern2.findall(tags)[0])
        except:
            self.num_suspected = 0

        try:
            self.num_recurred = int(pattern3.findall(tags)[0])
        except:
            self.num_recurred = 0

        try:
            self.num_death = int(pattern3.findall(tags)[0])
        except:
            self.num_death = 0
        
