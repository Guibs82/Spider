#encoding:utf-8

import requests

"""
	Web 客户端验证, 需要添加auth=(账户名, 密码)
"""

auth = ('Guibs', 'gpwd')

response = requests.get('http://xxx.xxx.xxx.xxx', auth=auth)

print response.text
