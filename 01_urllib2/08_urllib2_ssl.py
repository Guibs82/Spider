#encoding:utf-8

import urllib
import urllib2

"""
	处理SSL 证书验证失败
	例如12306 不符合CA 认证的证书
"""

# 1. 导入Python SSL 处理模块
import ssl

# 2. 表示忽略未经审核的SSL 证书认证
context = ssl._create_unverified_context()

url = "https://kyfw.12306.cn/otn/"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

request = urllib2.Request(url, headers=headers)

# 3. 在urlopen() 方法中 指明context 参数
response = urllib2.urlopen(request, context=context)

print response.read()
