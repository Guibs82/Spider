#encoding:utf-8

import urllib
import urllib2

# Request 对象的参数里有data 参数, 就是在用POST 的方式请求

"""
	有道词典的Post 模拟
"""

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

formdata = {
	"type":"AUTO",
	"i":"Python",
	"doctype":"json",
	"xmlVersion":"1.8",
	"keyfrom":"fanyi.web",
	"ue":"UTF-8",
	"action":"FY_BY_CLICKBUTTON",
	"typoResult":"true",
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=headers)
response = urllib2.urlopen(request)

print response.read()
