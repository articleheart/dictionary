# -- coding:utf-8 --
#by 张千万不要 2023-02-13
import re
print('今天天气不错，找点吃的')
def buildnode1():
	with open(r"C:\Users\lenovo\PycharmProjects\pythonProject\node1\word.txt", encoding='utf-8', mode='r') as node1:
		content = node1.read()
	content2 = content.replace("\n", "").replace(" 	", "").replace("	", "").replace(" ", "")
# content3=jieba.cut(content2,cut_all="TRUE")
	word = ""
	for i in content2:
		word += i + "\r\n"
	word2 = word.rstrip('\r\n')
# print (word)
	with open(r"C:\Users\lenovo\PycharmProjects\pythonProject\node1\dict1.txt", encoding='utf-8', mode='w') as dict1:
		dict1.write(word2)

print(len(content2))





with open(r"C:\Users\lenovo\PycharmProjects\pythonProject\node2\XDHYCD7th.txt", encoding='utf-8', mode='r') as node2:
	content = node2.read()

	print(type(content))


def readlargefile(filepath, blocksize):
	with open(filepath, encoding='utf-8', mode='r') as fileobj:
		while True:
			data = fileobj.read(blocksize)
			if not data:
				break
			yield data


# part = readlargefile(r"C:\Users\lenovo\PycharmProjects\pythonProject\node2\XDHYCD7th.txt",10000)
# for i in part:
# 	print(i)

# data = readlargefile(r"C:\Users\lenovo\PycharmProjects\pythonProject\node2\XDHYCD7th.txt",10000000)
# print(type(data))

with open(r"C:\Users\lenovo\PycharmProjects\pythonProject\node2\XDHYCD7th.txt", encoding="utf-8", mode='r') as fp:
	data = fp.read()
print(data)
p1 = re.compile(r'[【](.*?)[】]', re.S)
result = re.findall(p1, data)

print(len(result))
result2 = []
for i in result:
	if i not in result2:
		result2.append(i)
print(len(result2))
wordstr = ""
for word in result2:
	wordstr += word + "\r\n"
with open(r"C:\Users\lenovo\PycharmProjects\pythonProject\node2\dict2.txt", encoding="utf-8", mode='w') as fp:
	fp.write(wordstr)
print(len(wordstr))
