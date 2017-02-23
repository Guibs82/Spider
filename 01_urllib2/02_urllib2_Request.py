#encoding:utf-8

import urllib2

# url 作为Request() 方法的参数, 构建并返回一个Request 对象
request = urllib2.Request("http://www.baidu.com")

# Request 对象作为urlopen() 方法的参数, 发送给服务器并接收响应
response = urllib2.urlopen(request)

# 获取页面响应内容
html = response.read()

# 打印页面响应内容
print html
