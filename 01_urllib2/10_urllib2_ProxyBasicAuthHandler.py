#encoding:utf-8

import urllib2
import urllib

"""
	使用私密代理时, 若遇到407 错误:
	urllib2.HTTPError: HTTP Error 407: Proxy Authentication Required 
		表示代理没有通过身份验证

	需要通过:
		HTTPPasswordMgrWithDefaultRealm(): 来保存私密代理的所需信息
		ProxyBasicAuthHandler(): 来处理代理的身份验证
"""

# 私密代理授权的账户
user = "Guibs"

# 私密代理授权的密码
passwd = "gpwd"

# 私密代理IP
proxyserver = "xx.xxx.xxx.xxx:xxxx"

# 1. 构建一个密码管理对象, 用来保存需要处理的用户名和密码
passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 2. 添加账户信息, 第一个参数realm 是远程服务器相关域信息, 一般为None, 后面三个分别为 代理服务器, 用户名 密码
passwdmgr.add_password(None, proxyserver, user, passwd)

# 3. 构建一个包含私密验证的代理处理器对象ProxyBasicAuthHandler 对象, 参数是密码管理对象
proxy_auth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)

# 4. 通过build_opener() 方法使用自定义代理处理器对象创建自定义opener 对象
opener = urllib2.build_opener(proxy_auth_handler)

# 构造Request 请求
request = urllib2.Request("http://www.baidu.com")

# 5. 使用自定义opener 发送请求
response = opener.open(request)

# 打印响应内容
print response.read()
