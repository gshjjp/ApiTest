# _*_ coding : utf-8 _*_
# @Time : 2024/8/30 下午3:19
# @Author : 耿
# @File : test_post
# @Project :

import requests

import json
import time


get_url = 'https://tone.moushi.love/gw/core-auth/encrypt/generateRsaKey'

res = requests.get(get_url)

print(res.json())
print(type(res.json()))


response_data = res.json().get('data')

print(response_data.get('bizId'))

response_bizId = response_data.get('bizId')
time.sleep(5)

post_url = 'https://tone.moushi.love/gw/core-facade-admin/api/settlement/settlementConfig/config/list'

post_params = {"pageNo":1,"current":1,"pageSize":10}


res_post = requests.post(url=post_url,data=post_params)

print(res_post.json())









#
# print(res_dic)

