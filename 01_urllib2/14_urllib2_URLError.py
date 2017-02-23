#encoding:utf-8

import urllib2

"""
	URLError 产生的原因主要有:
	1. 没有网络连接
	2. 服务器连接失败
	3. 找不到指定服务器
"""

# 创建一个不可访问的Request 对象
request = urllib2.Request("http://www.klsfadjl.com")

try:
	urllib2.urlopen(request, timeout=5)
except urllib2.URLError, err:
	print err
