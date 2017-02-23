#encoding:utf-8

import re

"""
	1. 使用compile() 函数将正则表达式的字符串形式编译为一个Pattern 对象
	2. 通过Pattern 对象提供一系列方法对文本进行匹配查找, 获得匹配结果, 一个Match 对象
	3. 使用Match 对象提供的属性和方法获得信息, 根据需要进行其他操作
"""

pattern = re.compile(r'\d+', re.I) # 匹配至少一个数字 re.I 表示忽略大小写

"""
	Pattern 对象常用方法:
		match 方法:
			从起始位置开始查找, 一次匹配
		search 方法:
			从任何位置开始查找, 一次匹配
		findall 方法:
			全部匹配, 返回列表
		finditer 方法:
			全部匹配, 返回迭代器
		split 方法:
			分割字符串, 返回列表
		sub 方法:
			用于替换
"""

# match(string, [, pos[, endpos]])
#	pos: 起始位置, 默认0
#	endpos: 终止位置, 默认len
print "match ============="
match_result = pattern.match('one123two456three789') # 查找头部, 未能匹配
print match_result # None

match_result = pattern.match('one123two456three789', 2, 10) # 从e开始, 未能匹配
print match_result # None

match_result = pattern.match('one123two456three789', 3, 10) # 从1开始, 匹配成功, 返回一个Match 对象
print match_result # Match 对象
print match_result.group(0) # 可省略0, 获得整个匹配的字符串
print match_result.start(0) # 可省略0, 获得分组匹配字符串在整个字符串中起始位置
print match_result.end(0) # 可省略0, 获得分组匹配字符串在整个字符串中结束位置
print match_result.span(0) # 可省略0, 方法返回(start(group), end(group))


# search(string[, pos[, endpos]])
print "search ==========="
search_result = pattern.search('one123two456three789')
print search_result.group(0) # 123


# findall(string[, pos[, endpos]])
print "findall ==========="
findall_result = pattern.findall('one123two456three789')
print findall_result # ['123', '456', '789']


# finditer
print "finditer =========="
finditer_result = pattern.finditer('one123two456three789')
print finditer_result
for iter_item in finditer_result:
	print iter_item.group()


# split(string[, maxsplit])
#	maxsplit 用于指定最大分割次数, 不指定则全部分割
split_result = pattern.split('one123two456three789')
print split_result # ['one', 'two', 'three', '']


# sub(repl, string[, count])
"""
	repl:
		如果是字符串, 则会使用repl 去替换每一个匹配的子串, 并返回替换后的字符串, repl 还可以使用id 的形式来引用分组, 但不能使用编号0
		如果是函数, 这个方法应当只接收一个参数(Match 对象), 并返回一个字符串用于替换(返回的字符串中不能再引用分组)
	count:
		用于指定最多替换次数, 默认为全部替换
"""
sub_result = pattern.sub("---", 'one123two456three789')
print sub_result


# 贪婪模式
#	在整个表达式匹配成功的前提下, 尽可能多的匹配(*)

# 非贪婪模式
#	在整个表达式匹配成功的前提下, 尽可能少的匹配(?)

# Python 里数量词默认是贪婪的
