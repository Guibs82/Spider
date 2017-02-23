#encoding:utf-8

# urllib2 默认只支持HTTP/HTTPS 的GET 和POST 方法

# urlib 的urlencode() 可以将key: value 这样的键值对转换成key=value 这样的字符串.
# 解码则使用urllib 的unquote() 函数

import urllib # 负责url 编码处理
import urllib2

url = "http://www.baidu.com/s"
word = {"wd":"蜡笔小新"}
word = urllib.urlencode(word) # 转换成url 的编码格式(字符串)

# 拼接完整的url
full_url = url + "?" + word

print full_url

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko)"}

request = urllib2.Request(full_url, headers=headers)

response = urllib2.urlopen(request)
#print response.read()
