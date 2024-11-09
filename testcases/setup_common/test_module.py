# _*_ coding : utf-8 _*_
# @Time : 2024/9/10 3:43 下午
# @Author : 耿
# @File : test_module
# @Project :
# _*_ coding : utf-8 _*_
# @Time : 2024/9/3 11:10 上午
# @Author : 耿
# @File : test_get_params
# @Project :
import pytest
import requests

def setup_module():
    print('zhunbeishuju')

def teardown_module():
    print('qinglishuju')


def test_mobile_get():
    url='https://tone.moushi.love/gw/core-facade-admin/live/version/list'
    params = {

        'pageNo': 1,
        'pageSize': 10,
        'belongUserType': 1,
        'lecturerType': 1


    }
    headers = {
        # 'Content-Type':'application/json;charset=UTF-8'
        'Authorization': 'Bearer 11ebdd8a-cf02-45ed-92bf-e27fac1dffe8',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'

    }

    res = requests.get(url=url,params=params,headers = headers)
    print(res.json())

    result = res.json()
    print(result['data']['list'][0]['id'])
    assert res.status_code == 200

    assert result['message'] is None

    print('---------get---------')

    # assert result['data']['list'][0]['id'] == '1832765337704149023'

    # return res.status_code


def test_mobile_post():

    url = 'https://tone.moushi.love/gw/core-facade-admin/live/room/query'

    data = {
        'belongUserType':1,
        'lecturerType':1,
        'pageNo':1,
        'pageSize':10
    }
    headers = {
        'Content-Type':'application/json;charset=UTF-8',
        'Authorization': 'Bearer 0d31aa1b-b1e6-4617-9ad9-4572dde03b31',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'

    }

    res = requests.post(url=url,json=data,headers = headers)
    print("--------------------")
    print(res.json())

    assert res.json()['code'] == 0

    print('---------post---------')


if __name__ == '__main__':
    pytest.main()






