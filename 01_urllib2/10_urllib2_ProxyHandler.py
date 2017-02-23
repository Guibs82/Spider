#encoding:utf-8

import urllib2

"""
	代理设置 -- by ProxyHandler
"""

# 构建两个代理Handler, 一个有代理IP, 一个没有
proxy_handler = urllib2.ProxyHandler({"http": "222.195.68.135:8123"})
null_proxy_handler = urllib2.ProxyHandler({})

proxySwitch = True # 定义一个代理开关

# 通过urllib2.build_opener() 方法使用这些Handler 对象, 创建自定义opener 对象
# 根据代理开关判定是否使用代理

if proxySwitch:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)

request = urllib2.Request("http://www.baidu.com")
request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36")

# 应用自定义opener 对象到全局, 使得urlopen() 也可以使用自定义opener 的特性
urllib2.install_opener(opener)

response = urllib2.urlopen(request) # 因为将自定义opener 注册为全局

response = opener.open(request) # 若未将自定义opener 设置为全局

print response.read()
