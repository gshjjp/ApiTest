# _*_ coding : utf-8 _*_
# @Time : 2024/8/24 下午5:17
# @Author : 耿
# @File : test_get
# @Project :


import requests

url = 'https://vv.video.qq.com/checktime'

params = {


    "otype": "ojson"
}
res = requests.get(url = url,params=params)
print(res.status_code)
print(res.json())
print(res.text)




