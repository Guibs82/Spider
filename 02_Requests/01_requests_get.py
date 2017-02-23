#encoding:utf-8

import requests

# 写法1
response = requests.get("http://www.baidu.com")

# 写法2
response = requests.request("get", "http://www.baidu.com")

# 添加headers 和查询参数
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}
kw = {"wd": "蜡笔小新"}

# requests 中params 接收一个字典或者字符串的查询参数, 字典类型自动转换为url 编码, 不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)

# 查看相应内容, response.text 返回Unicode 格式的数据
#	使用response.text 时, Requests 会基于HTTP 响应的文本编码自动解码响应内容, 大多数Unicode 字符集都能被解码
print "Unicode 格式数据========="
print response.text

# 查看响应内容, response.content 返回字节流数据
#	使用response.content 时, 返回的是服务器相应数据的原始二进制字节流, 可以用来保存图片等二进制文件
print "字节流数据========="
print response.content

# 查看完整url 地址
print "查看完整url ========="
print response.url

# 查看响应头部字符编码
print "响应头部字符编码=========="
print response.encoding

# 查看响应码
print "响应码========"
print response.status_code
