import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("ggplot")

result={}
df=pd.read_csv("results/result_"+"crypto"+".csv",index_col=0)
result['crypto']=pd.read_csv("results/result_"+"crypto"+".csv",index_col=0)
result['fs']=pd.read_csv("results/result_"+"fs"+".csv",index_col=0)
result['ipc']=pd.read_csv("results/result_"+"ipc"+".csv",index_col=0)
result['kvm']=pd.read_csv("results/result_"+"kvm"+".csv",index_col=0)
result['md']=pd.read_csv("results/result_"+"md"+".csv",index_col=0)
result['mm']=pd.read_csv("results/result_"+"mm"+".csv",index_col=0)

def cutTime(df):
    list=df["editTime"].split("-",2)
    return list[0]+"-"+list[1]

date=df.apply(cutTime,axis=1)
for item in result:
    result[item]["editTime"]=date
    result[item]["patchName"]=df.apply(lambda x: x["patchName"].split("-")[1],axis=1)

df["editTime"]=date
df["patchName"]=df.apply(lambda x: x["patchName"].split("-")[1],axis=1)
print(df.groupby(["editTime"]).size().values)
plt.figure()  
plt.plot(df.groupby(["editTime"]).size().index,df.groupby(["editTime"]).size().values)
plt.gcf().autofmt_xdate()
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel("version", fontsize=20)
# plt.ylabel("times", fontsize=20)
plt.savefig("pictures/"+"patch-time.png")
plt.show()