#encoding:utf-8

import urllib2

"""
	1. 使用相关的Handler 处理器, 创建特定功能的处理器对象
	2. 通过urllib2.build_opener() 方法使用这些处理器对象, 创建自定义opener 对象
	3. 使用自定义的opener 对象, 调用open() 方法发送请求
	Ps: 如果程序所有的请求都是用自定义的opener, 可以用urllib2.install_opener() 将自定义的opener 对象定义为全局opener, 表示之后凡是调用urlopen, 都将使用这个opener
"""

# 构建一个HTTPHandler 处理器对象, 处理HTTP 请求
http_handler = urllib2.HTTPHandler(debuglevel=1) # debuglevel=1 开启Debug Log, 在程序执行时, 会将收发包的报头在屏幕上自动打印出来

# 构建一个HTTPSHandler 处理器对象, 处理HTTPS 请求
https_handler = urllib2.HTTPSHandler()

# 调用urllib2.build_opener() 方法, 创建自定义opener 对象
http_opener = urllib2.build_opener(http_handler) 
https_opener = urllib2.build_opener(https_handler)

# 构建Request 请求
request = urllib2.Request("http://www.baidu.com")

# 添加User-Agent
request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12")

# 调用自定义opener 对象的open() 方法, 发送request 请求
response = http_opener.open(request)

print "========"

# 获取服务器响应内容
print response.read()
