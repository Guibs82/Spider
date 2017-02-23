#encoding: utf-8

import requests

"""
	使用data 参数传递POST 请求中的参数
"""

formdata = {
	"type":"AUTO",
	"i":"i love python",
	"doctype":"json",
	"xmlVersion":"1.8",
	"keyfrom":"fanyi.web",
	"ue":"UTF-8",
	"action":"FY_BY_ENTER",
	"typoResult":"true"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

response = requests.post(url, data=formdata, headers=headers)

print response.text.strip() # strip() 去除收尾空格

# 如果是json 文件可以直接显示
print response.json()
