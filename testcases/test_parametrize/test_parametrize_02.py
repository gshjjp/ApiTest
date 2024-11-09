# _*_ coding : utf-8 _*_
# @Time : 2024/11/4 5:33 下午
# @Author : 耿
# @File : test_parametrize_02
# @Project :
import pytest


@pytest.mark.parametrize('name,word',[['wls','zuiai'],['wl','2aifc']])
def test_parametrize_02(name,word):
    print(f'{name} is {word}')
