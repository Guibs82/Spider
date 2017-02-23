#encoding:utf-8

import os
import urllib
import urllib2
from lxml import etree

class Spider:
	"""贴吧图片"""
	def __init__(self):
		self.tiebaName = raw_input("请输入需要访问的贴吧:")
		self.beginPage = int(raw_input("请输入起始页:"))
		self.endPage = int(raw_input("请输入终止页:"))

		self.url = "http://tieba.baidu.com/f"
		self.ua_header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

		# 图片编号
		self.imageName = 1
	
	def tiebaSpider(self):
		print "tiebaSpider"
		for page in range(self.beginPage, self.endPage + 1):
			pn = (page - 1) * 50 # page number
			word = {"pn": pn, "kw": self.tiebaName}

			word = urllib.urlencode(word) # 转换成url 编码格式(字符串)
			myURL = self.url + "?" + word

			# 调用页面处理函数, load_Page
			#	获取页面所有帖子链接
			self.loadPage(myURL)
	
	# 读取页面内容
	def loadPage(self, url):
		print "loadPage"
		print url
		req = urllib2.Request(url, headers = self.ua_header)
		html = urllib2.urlopen(req).read()
		print html

		# 解析html 为HTML 文档
		selector = etree.HTML(html)

		# 抓取当前页面所有帖子的url 后半部分(帖子编号)
		links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
		
		# links 为额treeElementString 列表
		# 遍历列表, 并合并成一个帖子地址, 调用图片处理函数loadImage
		for link in links:
			link = "http://tieba.baidu.com" + link
			print link
			self.loadImages(link)
	
	# 获取图片
	def loadImages(self, link):
		print "loadImages"
		req = urllib2.Request(link, headers = self.ua_header)
		html = urllib2.urlopen(req).read()

		selector = etree.HTML(html)

		# 获取这个帖子里所有的图片的src
		imagesLinks = selector.xpath('//img[@class="BDE_Image"/@src')
		print imagesLinks

		# 依次取出图片路径, 下载保存
		for imagesLink in imagesLinks:
			self.writeImages(imagesLink)
	
	# 保存图片
	def writeImages(self, imagesLink):
		print "writeImages"
		print imagesLink
		print "正在存储第%d个图片" % self.imageName
		
		# 1. 打开文件, 返回一个文件对象
		file = open('./images/' + str(self.imageName) + '.png', 'wb')
		# 2. 获取图片内容
		image = urllib2.urlopen(imagesLink).read()
		# 3. 调用文件对象write() 方法, 将page_html 的内容写入文件里
		file.write(image)
		# 4. 最后变比文件
		file.close()

		# 计数器+1
		self.imageName += 1

if __name__ == "__main__":
	# 创建爬虫对象
	spider = Spider()
	# 调用爬取方法, 开始工作
	spider.tiebaSpider()
