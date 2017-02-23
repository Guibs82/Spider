#encoding:utf-8

import requests

"""
	使用Session 实例实现人人网登陆
"""

# 1. 创建session 对象(可以保存Cookie 的值)
session = requests.session()

# 2. 设置User-Agent
headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
}

# 3. 需要登录的用户名和密码
data = {
	"email": "gemail",
	"password": "gpwd",
}

# 4. 发送福袋用户名密码的请求, 获取登陆后的Cookie 值保存在Session对象中
session.post("http://www.renren.com/PLogin.do", data=data)

# 5. 在同个包含用户登入后的Cookie 值的session 中, 直接访问其他登录后可访问的页面
response = session.get("http://www.renren.com/338899086/profile")

# 打印响应内容
print response.text
