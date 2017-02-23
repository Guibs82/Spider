#encoding:utf-8

import requests

"""
	通过proxies 参数设置代理
"""

# 开放代理
proxies = {
	"http": "http://180.169.59.221:8080",
	"https": "http://180.169.59.221:8080",
}

# 私密代理
#proxies = {"http": "userName:passWD@xx.xxx.xxx.xxx:xxxx"} # 用户名:密码@IP:Port

response = requests.get("http://www.baidu.com", proxies=proxies)

print response.text
