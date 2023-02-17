# -- coding:utf-8 --
# by 张千万不要 2023-02-17 04:00:00
# 建立第三个节点node3
# 功能:文本清洗，删除特殊字符、标点符号、停用词。
import time
def readstopwords(filepath: str) -> list:
	'''function：返回停用词
	   args: filepath
	   return: list
	'''
	with open(filepath, encoding='utf-8', mode='r') as stopwordsfp:
		stopwords = list(stopwordsfp.read())
	#print(stopwords)
	return stopwords

if __name__ == '__main__':
	node3name = "hit.txt"  # 设置node3名称，可选为baidu.txt ， cn.txt ， scu.txt ，hit.txt 。
	nodepath = 'C:/Users/lenovo/PycharmProjects/articleheart/node3/' #设置节点路径
	# print(nodepath)
	# print(nodepath + node3name)
	time1 = time.time()
	stopwords = readstopwords(nodepath + node3name)
	time2 = time.time()
	time3 =time2-time1
	#print(stopwords)
	print("节点三建立完成，用时:" + str(time3) +"秒。" "请查看目录：" + nodepath)