import os
import time
def gettxtpathlist(frompath):
    '''
    功能：获取要合并的文件列表
    frompath：要合并的父文件夹
    return:要合并的文件列表
    '''
    path = frompath
    txtpathlist = []
    names = os.listdir(path)
    for file in names :
        txtnamelist = os.listdir(path + file)
        for i in txtnamelist:
            txtpath = path + file + '/' + i
            txtpathlist.append(txtpath)
    return(txtpathlist)


def mergetxt(txtpathlist,destpath):
    '''
    功能：获取要合并文件写入新文件
    txtpathlist：要合并的文件列表
    destpath:合并后的文件
    '''
    for i in txtpathlist:
        with open(i,mode='r',encoding='UTF-8') as file:
            file = file.read()
        print('正在读取'+ i)
        
        #print(file)
        print("正在转存文件")
        with open(destpath,mode='a',encoding='UTF-8') as file2:
            file2.write(file)
        print('正在关闭'+ i)
        file2.close
    
if __name__ == '__main__':   
    frompath="d:/data/"
    destpath="e:/yuliao.txt"
    txtpathlist=gettxtpathlist(frompath)
    print("正在生成语料库")
    time1 = time.time()
    mergetxt(txtpathlist,destpath)
    time2=time.time()
    time3=time2-time1
    print("语料库生成,用时"+str(time3))
    


    #file = open("E:/yuliao.txt",mode='a+',encoding='UTF-8')
