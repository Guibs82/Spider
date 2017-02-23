#encoding:utf-8

import urllib
import urllib2

headers = {
	"Accept":"*/*",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Connection":"keep-alive",
	"Cookie":"buvid3=8FCDA69A-07AF-49B4-92A9-6FA3E5F8525336032infoc; fts=1487089798; pgv_pvi=5824817152; pgv_si=s3472204800; sid=bb807qpm",
	"Host":"api.bilibili.com",
	"Referer":"http://www.bilibili.com/",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
}

formdata = {
	"callback":"jQuery17208214261744178626_1487089918532",
	"pf":"0",
	"ids":"44,42,40",
	"jsonp":"jsonp",
	"_":"1487089918903"
}

url = "http://api.bilibili.com/x/web-show/res/locs"

data = urllib.urlencode(formdata)

url = url + "?" + data

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

print response.read()
