#encoding:utf-8

import urllib2
import cookielib

"""
	cookielib 模块: 提供用于存储cookie 的对象
	HTTPCookProcessor 处理器: 处理cookie 对象, 
"""

"""
	CookieJar: 管理HTTP cookie 值, 存储HTTP 请求生成的cookie, 向传出的HTTP 请求添加cookie 的对象.
		整个cookie 都存储在内存中, 对CookieJar 实例进行垃圾回收后cookie 也将丢失
"""

def test1():
	"""
		获得并打印cookie
	"""
	# 构建一个CookieJar 对象实例来保存cookie
	cookiejar = cookielib.CookieJar()

	# 使用HTTPCookieProcessor() 来创建cookie 处理器对象, 参数为CookieJar 对象
	handler = urllib2.HTTPCookieProcessor(cookiejar)

	# 通过build_opener() 来构建opener
	opener = urllib2.build_opener(handler)

	# 以get 方法访问页面, 访问后会自动保存cookie 到CookieJar 中
	opener.open("http://www.baidu.com")

	# 按标准格式打印保存的Cookie
	cookieStr = ""
	for item in cookiejar:
		cookieStr = cookieStr + item.name + "=" + item.value + ";"
	
	# 舍弃cookieStr 的最后一位分好
	print cookieStr[:-1]

def test2():
	"""
		保存获得的Cookie 到Cookie文件中
	"""

	# 保存cookie 的本地磁盘文件名
	filename = 'cookie.txt'

	# 声明一个MozillaCookieJar(有save 实现)对象来保存cookie, 之后写入文件
	mozillaCookieJar = cookielib.MozillaCookieJar(filename)

	# 创建cookie 处理器对象
	handler = urllib2.HTTPCookieProcessor(mozillaCookieJar)

	# 通过build_opener() 构建opener
	opener = urllib2.build_opener(handler)

	# 创建请求
	response = opener.open("http://www.baidu.com")

	# 保存cookie 到本地文件
	mozillaCookieJar.save()

def test3():
	"""
		从文件中获取cookies, 作为请求的一部分去访问
	"""
	
	# 1. 创建MozillaCookieJar(有load 实现)实例对象
	mozillaCookieJar = cookielib.MozillaCookieJar()

	# 2. 从文件中读取cookie 内容到变量
	mozillaCookieJar.load('cookie.txt')

	# 3. 使用HTTPCookieProcessor() 来创建cookie 处理器对象
	handler = urllib2.HTTPCookieProcessor(mozillaCookieJar)

	# 构建opener
	opener = urllib2.build_opener(handler)

	response = opener.open("http://www.baidu.com")


if __name__ == '__main__':
	test3()
