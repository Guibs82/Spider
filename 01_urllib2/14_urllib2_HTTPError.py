#encoding:utf-8

import urllib2

"""
	如果urlopen 或opener.open() 不能处理的, 会产生一个HTTPError, 对应相应的状态码, HTTP 状态码表示HTTP 协议锁返回的响应状态
	注意:
		urllib2 可以帮我们处理重定向的页面(3 开头的响应码), 而100 - 299: 表示成功. 所以只能看到400 - 599 的错误号
"""

request = urllib2.Request('http://blog.baidu.com/guibs')

try:
	urllib2.urlopen(request)
except urllib2.HTTPError, err:
	print err.code
	print err
