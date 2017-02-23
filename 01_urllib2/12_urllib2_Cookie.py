#encoding:utf-8

import urllib2

"""
	获取一个有登录信息的Cookie 模拟登陆
"""

# 1. 通过抓包构建一个已登录的用户headers 信息
headers = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	# "Accept-Encoding":"gzip, deflate, sdch, br",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Cookie":'aliyungf_tc=AQAAAIpwq2n1ywoAU3AwtmH17VYMt0Uz; l_n_c=1; q_c1=36423d934fcb4303aa5b96f66f2138f0|1487127925000|1487127925000; _xsrf=f0a6bd907dfd34a81542306b55fe97c0; cap_id="YzFjOWQ3ZjNlMmRjNGM4YmJlYmM3ODM5ODJjMzAwNzM=|1487127925|0881bf08a3965d4e7a6838017cd72a721d391511"; l_cap_id="ZWNkYzQ0ZjEwYTA1NGNkZjkxZTEzNTg5ODYyNTkzMGE=|1487127925|735365bdc3b3afe220dad4cde8ae4942ebd5f730"; d_c0="AJACE4YCUAuPTmToVZ46iTHM8kVzdDyfzjE=|1487127931"; _zap=a0391bf6-0685-4130-a9bf-2091954b28ac; login="Y2ZlYTIwMWUzYTc5NDBkNzlkY2VlMjhhNzVhYWFiYzA=|1487127950|a41163f6520b61fce764732face1d4f9898363f9"; __utma=51854390.42444198.1487127933.1487127933.1487127933.1; __utmb=51854390.0.10.1487127933; __utmc=51854390; __utmz=51854390.1487127933.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20170215=1; z_c0=Mi4wQUFCQVVrRWxBQUFBa0FJVGhnSlFDeGNBQUFCaEFsVk5aRlBMV0FEb18xYlFiMk80djNrMGF5aW94UHg2TjgtVGpn|1487128164|9768fbdbbcb65f098b64302a6db22e2202c76e70; nweb_qa=heifetz',
	"Host":"www.zhihu.com",
	"Referer":"https://www.zhihu.com/",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
}

# 2. 通过headers 里的报头信息(主要Cookie 信息), 构建Request 对象
request = urllib2.Request("https://www.zhihu.com/people/gui-bu-si", headers = headers)

# 3. 直接访问知乎个人主页. 服务器会根据headers 判断登录状态
response = urllib2.urlopen(request)

# 打印响应内容
print response.read()
