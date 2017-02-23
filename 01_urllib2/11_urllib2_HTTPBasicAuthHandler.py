#encoding:utf-8

import urllib
import urliib2

"""
	有些Web 服务器(HTTP/FTP 等)访问时需要身份验证, 爬虫直接访问会报401 错误
	urllib2.HTTPError: HTTP Error 401: Unauthorized
"""

# 用户名
user = "Guibs"

# 密码
passwd = "gpwd"

# Web 服务器IP
webserver = "http://xxx.xxx.xxx.xxx"

# 1. 构建一个密码管理对象, 用来保存登录需要的用户名和密码
passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 2. 添加账户信息, 第一个参数realm 是与远程服务器相关的域信息, 一般为None, 后面是Web服务器, 用户名, 密码
passwdmgr.add_password(None, webserver, user, passwd)

# 3. 构建一个HTTP基础用户名/密码验证的HTTPBasicAuthHandler 处理器对象, 参数是创建的密码管理对象
http_auth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

# 4. 通过build_opener() 方法使用Handler 对象创建自定义opener 对象
opener = urllib2.build_opener(http_auth_handler)

# 5. 可以选择通过install_opener() 方法定义自定义opener为全局opener
#urllib2.install_opener(opener)

# 构建Request 对象
reqeust = urllib2.Request("http://xxx.xxx.xxx.xxx")

# 使用opener 发送请求
#response = urllib2.urlopen(request) # 若注册后, 可使用urllib2.urlopen()
response = opener.open(request)

# 打印响应内容
print response.read()
