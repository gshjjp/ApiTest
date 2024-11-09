# _*_ coding : utf-8 _*_
# @Time : 2024/10/18 4:34 下午
# @Author : 耿
# @File : test_parametrize_01
# @Project :
import pytest


#单参数多次循环
@pytest.mark.parametrize("name",["anqila","huangzhong","daqiao"])
def test_parametrize(name):
    print("woshi"+' '+name)
    assert name == 'anqila'

#单参数 多次循环
