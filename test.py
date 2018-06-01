import re
f = open('patchs/patch-2.6.0', 'r')              #文件为123.txt

sourceInLines = f.readlines()  #按行读出文件内容
f.close()
new = []                                   #定义一个空列表，用来存储结果
for line in sourceInLines:
    temp1 = line.strip('\n')       #去掉每行最后的换行符'\n'
    new.append(temp1)          #将上一步得到的列表添加到new中

count=0
for item in new :
    # info=re.findall(r'diff',str(item))
    if('diff'in str(item))and('/md/'in str(item)):
        count+=1
print(count)
# w = re.findall(r'\btina','tian tinaaaa')
# print(w)