#encoding:utf-8

from lxml import etree

text = '''
<div>
	<ul>
		<li class="item-0"><a href="link1.html">first item</a></li>
		<li class="item-1"><a href="link2.html">second item</a></li>
		<li class="item-inactive"><a href="link3.html">third item</a></li>
		<li class="item-1"><a href="link4.html">fourth item</a></li>
		<li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
	</ul>
</div>
'''

# 利用etree.HTML 将字符串解析为HTML 文档
html = etree.HTML(text)

# 按字符串序列化HTML 文档
result = etree.tostring(html)

print result


# 从文件中读取页面代码
html = etree.parse("./test.html")
result = etree.tostring(html, pretty_print=True)

print result


print "Xpath 测试"
result = html.xpath('//li/text()')

print result # 打印<li>标签的元素集合
print len(result)
print type(result)
print type(result[0])
