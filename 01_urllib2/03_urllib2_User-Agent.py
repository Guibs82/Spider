#encoding:utf-8

import urllib2

url = "http://www.bilibili.com"

# Safari 的User-Agent
ua = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

# 构建带有特定User-Agent 的Request 对象
request = urllib2.Request(url, headers = ua)

# 发送请求
response = urllib2.urlopen(request)

# 并打印响应内容
html = response.read()
print html
