# -- coding:utf-8 --
# by 张千万不要 2023-02-13 23:25:00
# 格式化新华字典，建立第一个节点,16159个汉字

def readxhzd(filepath: str) -> str:
	"""功能：读取新华字典
	:arg:filepath
	:return: content"""
	with open(filepath, encoding='utf-8', mode='r') as xhzdfp:
		content: str = xhzdfp.read()
	# print(content)
	return content

def xhzdtolist(content: str) -> list:
	content: str = content.replace("\n", "").replace(" 	", "").replace("	", "").replace(" ", "")
	xhzdlist: list = list(content)
	return xhzdlist

def formatxhzd(xhzdlist: str) -> str:
	words: str = ""
	for word in xhzdlist:
		words += word + "\r\n"
	words = words.rstrip('\r\n')
	return words

def buildnode1(node1path: str, words: str):
	with open(node1path, encoding='utf-8', mode='w') as node1fp:
		node1fp.write(words)

if __name__ == '__main__':
	xhzdname: str = "xhzd.txt"  # 设置新华字典名称
	node1name: str = "node1.txt"  # 设置dict1名称
	nodepath = 'C:/Users/lenovo/PycharmProjects/articleheart/node1/' #设置节点路径
	# print(node1path)
	# print(nodepath + xhzdname)
	content = readxhzd(nodepath + xhzdname)
	xhzdlist: list = xhzdtolist(content)
	words: str = formatxhzd(xhzdlist)
	buildnode1(nodepath + node1name, words)
# print(words)
