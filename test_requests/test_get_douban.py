# _*_ coding : utf-8 _*_
# @Time : 2024/9/2 4:55 下午
# @Author : 耿
# @File : test_get_douban
# @Project :
import requests

url  = 'https://movie.douban.com/j/search_subjects'

params = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': '50',
    'page_start': 0
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'

}

r = requests.get(url = url,params=params,headers = headers)
print(r.status_code)
print(r.json())