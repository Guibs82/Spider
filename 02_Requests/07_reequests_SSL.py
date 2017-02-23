#encoding:utf-8

import requests

"""
	使用verify 参数检查某个主机的SSL 证书, 默认True
		设置为False, 则跳过证书验证
"""

response = requests.get("https://kyfw.12306.cn/otn/", verify=False)

print response.text
