# _*_ coding : utf-8 _*_
# @Time : 2024/10/18 4:25 下午
# @Author : 耿
# @File : read_data
# @Project :
import  yaml

f = open("../config/data.yaml",encoding='utf-8')

data = yaml.safe_load(f)
print("------------------")
print(data)
print(data['hero'])
print(data['heros_name'])
print(data['heros'])
print(data['heros_name_list'])