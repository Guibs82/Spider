#encoding:utf-8

import urllib2
import random

url = "http://www.bilibili.com"

# 指定User-Agent 的header

ua_list = [
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko)",
]

# 创建Request 对象
request = urllib2.Request(url)

# 通过add_header() 对Request 对象添加/修改一个特定的header
request.add_header("Connection", "keep-alive")

# 设置随机的User-Agent
user_agent = random.choice(ua_list)
request.add_header("User-Agent", user_agent)


# 通过调用Request 对象的get_header(header_name) 方法来查看header 信息
# header_name 第一个字母大写, 后面的全部小写
print request.get_header("User-agent")
print request.get_header("Connection")
print request.headers

# 发送请求
response = urllib2.urlopen(request)

# 查看响应状态码
print response.code

html = response.read()

