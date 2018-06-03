import gzip
import os
def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    #获取文件的名称，去掉
    g_file = gzip.GzipFile("patchData/"+file_name)
    #创建gzip对象
    open("patchs/"+f_name, "wb+").write(g_file.read())
    #gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
    #关闭gzip对象

for item in list(os.walk("patchData"))[0][2]:
    un_gz(item)