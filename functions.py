import csv
import json
from datetime import datetime

def ToCSV_separately(Province_list):
    path_peifix = 'D:\MyGit\Real-time-dynamic-query-of-pneumonia\Data Record Separately\\'
    for province in Province_list:
        file_path = path_peifix+province.provinceShortName+'.csv'
        csv_file = open(file_path, 'a+', newline='')
        title = ['sort','确诊','疑似','治愈','死亡','修改时间']
        writer = csv.writer(csv_file)
        writer.writerow(title)
        
        modify_time = datetime.fromtimestamp(province.modifyTime/1000)
        time_str = datetime.strftime(modify_time,'%Y-%m-%d %H:%M:%S')
        writer.writerow([province.sort,province.num_confirmed,province.num_suspected,province.num_cured,province.num_dead,time_str])
        csv_file.close()

def DicToCSV(dic_data,file_name):
    path = 'D:\MyGit\Real-time-dynamic-query-of-pneumonia\Data Record csv\\' + file_name
    csv_file = open(path, 'w+', newline='')
    keys = []
    writer = csv.writer(csv_file)
    for dic in dic_data:
        keys = dic.keys()
        # 写入列名
        writer.writerow(keys)
        break

    for dic in dic_data:
        for key in keys:
            if key not in dic:
                dic[key] = ''
        writer.writerow(dic.values())
    csv_file.close()