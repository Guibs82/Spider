#encoding:utf-8

import requests

response = requests.get("http://www.baidu.com/")

# 从response 中获取CookieJar 对象
cookiejar = response.cookies

# 将cookieObj 转换为字典
cookieDic = requests.utils.dict_from_cookiejar(cookiejar)

print cookiejar

print cookieDic
