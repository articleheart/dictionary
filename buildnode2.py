# -- coding:utf-8 --
# by 张千万不要 2023-02-16 12:12:00
# 格式化现代汉语词典，建立第二个节点,67541词语
import re
import time
def readhycd(filepath: str) -> str:
	"""功能：读取汉语字典
	:arg:filepath
	:return: content"""
	with open(filepath, encoding='utf-8', mode='r') as hycdfp:
		content = hycdfp.read()
	#print(content)
	return content

def hycdtolist(content: str) -> list:
	p1 = re.compile(r'[【](.*?)[】]', re.S)
	result = re.findall(p1, content)
	#print(len(result))
	hycdlist = list(result)
	hycdlist2 = []  #词典去除重复词条，剩余67541个词语
	for i in hycdlist:
		if i not in hycdlist2:
			hycdlist2.append(i)
	print("节点二共有词语："+str(len(hycdlist2)))
	return hycdlist2

def formathycd(hycdlist: str) -> str:
	words = ""
	for word in hycdlist:
		words += word + "\r\n"
	words = words.rstrip('\r\n')
	return words

def buildnode2(node2path: str, words: str):
	with open(node2path, encoding='utf-8', mode='w') as node2fp:
		node2fp.write(words)

if __name__ == '__main__':
	hycdname = "hycd.txt"  # 设置汉语词典名称
	node2name = "node2.txt"  # 设置node2名称
	nodepath = 'C:/Users/lenovo/PycharmProjects/articleheart/node2/' #设置节点路径
	# print(node1path)
	# print(nodepath + xhzdname)
	print("正在建立节点二，大概用时80秒，请稍等......")
	time1 = time.time()
	content = readhycd(nodepath + hycdname)
	hycdlist = hycdtolist(content)
	words = formathycd(hycdlist)
	buildnode2(nodepath + node2name, words)
	time2 = time.time()
	time3 =time2-time1
	#print(words)
	print("节点二建立完成，用时:" + str(time3) +"秒。" "请查看目录：" + nodepath)
