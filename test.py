import os
import pandas as pd
import time

def diffService(modules, files):
    info = []  # 存储信息
    count = 0  # diff数量
    editCount = 0  # 修改的数量（几处地方）
    subCount = 0  # 减少的行数
    addCount = 0  # 添加的行数
    annotationCount = 0  # 添加注释的数量
    haveTime = False  # 是否拥有time
    haveIndex = False  # 是否拥有index
    maxChangeLine = 0  # 最多修改行数
    for item in files:
        # 判断是否是要操作的模块
        if('diff'in str(item))and('/'+modules+'/'in str(item)):
            count += 1
            startLine = files.index(item)  # diff头
            endLine = startLine+1  # diff尾
            # 获取diff尾
            while not(('diff'in str(files[endLine])) or (files.count == endLine+1)):
                endLine += 1
            endLine -= 1
            time = []
            time = str(files[startLine+2]).replace('\t',
                                                   ' ').split(" ")  # 去掉制表符后分隔
            if len(time) > 3:
                haveTime = True
            if files[startLine+2].startswith("index"):
                haveIndex = True
            tempStartLine = startLine
            tempChangeLine =0 
            #确定第一个@@
            while not files[tempStartLine].startswith("@@"):
                tempStartLine += 1
            for index in range(tempStartLine, endLine+1, 1):
                item = str(files[index])
                if item.startswith("-"):
                    subCount += 1
                    tempChangeLine+=1
                elif item.startswith("+"):
                    addCount += 1
                    tempChangeLine+=1
                    if item.startswith("+/*") or item.startswith("+ *"):
                        annotationCount += 1
                elif item.startswith("@@"):
                    editCount += 1
            if tempChangeLine>maxChangeLine:
                maxChangeLine=tempChangeLine
    info=[count,editCount,subCount,addCount,annotationCount,haveTime,haveIndex,maxChangeLine]
    # info.columns = ['count','editCount',"subCount","addCount","annotationCount","haveTime","haveIndex","maxChangeLine",]
    # return pd.DataFrame(info).transpose()
    return info
    # w = re.findall(r'\btina','tian tinaaaa')
    # print(w)

def fileService(filePath):
    f = open(filePath, 'r')  # 文件为123.txt
    sourceInLines = f.readlines()  # 按行读出文件内容
    f.close()
    new = []  # 定义一个空列表，用来存储结果
    for line in sourceInLines:
        temp1 = line.strip('\n')  # 去掉每行最后的换行符'\n'
        new.append(temp1)  # 将上一步得到的列表添加到new中
    #选择模块
    info=diffService("md", new)
    info.append(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.path.getmtime(filePath))))
    info.append(os.path.getsize(filePath))
    return info

def folderService():
    result=[]
    for item in list(os.walk("patchs"))[0][2]:
        info=fileService('patchs/'+item)
        info.insert(0,item)
        result.append(info)
    result=pd.DataFrame(result)
    result.columns = ['patchName','count','editCount',"subCount","addCount","annotationCount","haveTime","haveIndex","maxChangeLine","editTime","size"]
    return result

folderService().to_csv("results/result.csv")