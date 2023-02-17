# -- coding:utf-8 --
# by 张千万不要 2023-02-17 04:00:00
# 建立第四个节点node4
# 功能:一个初始值为空的自定义词典，通过训练不断增长的节点。
import time
def buildnode4(filepath):
    with open(filepath, encoding='utf-8', mode='w') as node4fp:
        pass
    node4fp.close()

def addwords(filepath, wordslist):
    #打开文件，读取内容
    if wordslist:
        with open(filepath, encoding='utf-8',mode='r') as fpnode4:
            tempwords = fpnode4.read()
            fpnode4.close()
        print(len(tempwords))
        #接收传入列表wordslist
        words=""
        for word in wordslist:
            if word not in tempwords:
                words += word + "\r\n"
        with open (filepath,encoding='utf-8',mode='a') as fpnode4:
            fpnode4.write(words)
            fpnode4.close()
    else:
        pass

if __name__ == '__main__':
    node4name = "usercs.txt"  # 设置node4名称
    nodepath = 'C:/Users/lenovo/PycharmProjects/articleheart/node4/'  # 设置节点路径
    time1 = time.time()
    list1=['中国共产党','新时代','中国特色','社会主义','中国化','时代化','马克思主义','习近平新时代中国特色社会主义思想']
    #list1=[]
    addwords(nodepath + node4name,list1)
    time2 = time.time()
    time3 = time2 - time1
    print("节点四建立完成，用时:" + str(time3) + "秒。" "请查看目录：" + nodepath)