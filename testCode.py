import os
import pandas as pd
import time
import chardet
from bs4 import UnicodeDammit  

def folderService():
    result = []
    # 遍历patchs目录下所有patch文件
    for item in list(os.walk("patchs"))[0][2]:
        print(item)
        encode=chardet.detect(open("patchs/"+item,"rb").read())["encoding"]
        print(encode)

folderService()